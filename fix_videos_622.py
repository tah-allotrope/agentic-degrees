#!/usr/bin/env python3
"""1) Supplement 6.622 (direct-file URL pattern). 2) Rewrite videos.txt per course
with YouTube links from the course video gallery (data.json)."""
import json, os, re, sys, time, html, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"}
BASE = "https://ocw.mit.edu/courses"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mit-ocw-curriculum")

def fetch(url, timeout=60, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise last

def strip_hash(name):
    return re.sub(r"^[0-9a-f]{32}_", "", name)

def categorize(name):
    n = name.lower()
    if re.search(r"\b(soln|solution|answer)\b", n):
        return "exams/solutions" if re.search(r"\b(exam|quiz|final|midterm|test|assess)\b", n) else "assignments/solutions"
    if re.search(r"\b(hand)\b", n):
        return "lecture-notes/handwritten"
    if re.search(r"\b(lec|lecture|slides?|handout|note|notes)\b", n):
        return "lecture-notes"
    if re.search(r"\b(ps|problem|assignment|homework|hw|exercises?|lab)\b", n):
        return "assignments"
    if re.search(r"\b(exam|quiz|final|midterm|test|assess|designproj|project)\b", n):
        return "exams" if re.search(r"\b(exam|quiz|final|midterm|test|assess)\b", n) else "assignments"
    if re.search(r"\b(read|book|reference|manual)\b", n):
        return "readings"
    if n.endswith((".py", ".c", ".h", ".java", ".js", ".ipynb", ".m", ".ml", ".ipynb")):
        return "software"
    if re.search(r"\b(install|code|software|tool)\b", n):
        return "software"
    return "other"

# ---------- part 1: 6.622 supplement ----------
def fix_6622():
    slug = "6-622-power-electronics-spring-2023"
    cdir = os.path.join(ROOT, "electrical-engineering", "08-power-electronics-6.622")
    os.makedirs(cdir, exist_ok=True)
    dl_html = fetch(f"{BASE}/{slug}/download/").decode("utf-8", errors="ignore")
    esc = re.escape(f"/courses/{slug}/")
    links = set()
    for m in re.finditer(rf'href="({esc}[^"]+)"', dl_html):
        u = m.group(1)
        tail = u[len(f"/courses/{slug}/"):]
        if tail in ("download",) or tail.endswith("/") or "/" in tail:
            continue
        fname = strip_hash(tail)
        ext = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
        if ext in ("pdf", "zip", "py", "c", "h", "java", "ipynb", "m", "txt", "csv"):
            links.add((fname, "https://ocw.mit.edu" + u))
    # also scan course page lists (assessments/problem-sets/lecture-notes) pages
    for lst in ("lists/assessments", "lists/problem-sets", "lists/typed-lecture-notes", "lists/handwritten-lecture-notes"):
        try:
            lhtml = fetch(f"{BASE}/{slug}/{lst}/").decode("utf-8", errors="ignore")
            for m in re.finditer(rf'href="({esc}[^"]+)"', lhtml):
                u = m.group(1)
                tail = u[len(f"/courses/{slug}/"):]
                if tail == "download" or tail.endswith("/") or "/" in tail:
                    continue
                fname = strip_hash(tail)
                ext = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
                if ext in ("pdf", "zip", "py", "c", "h", "java", "ipynb", "m", "txt", "csv"):
                    links.add((fname, "https://ocw.mit.edu" + u))
        except Exception:
            pass
    print(f"6.622: {len(links)} files found")
    ok, fail = 0, []
    def dl_one(item):
        fname, url = item
        cat = categorize(fname)
        dest = os.path.join(cdir, cat, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return fname, cat, "exists"
        try:
            data = fetch(url, timeout=120)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as f:
                f.write(data)
            return fname, cat, "ok"
        except Exception as e:
            return fname, cat, f"ERR {type(e).__name__}"
    with ThreadPoolExecutor(max_workers=6) as ex:
        for fut in as_completed([ex.submit(dl_one, it) for it in links]):
            fname, cat, st = fut.result()
            if st == "ok":
                ok += 1
            elif st != "exists":
                fail.append(fname)
    print(f"6.622: ok={ok} fail={len(fail)} {fail[:5]}")
    # metadata + README update
    page_html = fetch(f"{BASE}/{slug}/").decode("utf-8", errors="ignore")
    title = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", page_html, re.S)
    if m:
        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
    with open(os.path.join(cdir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# 6.622 | {title or slug}\n\n")
        f.write(f"- MIT OCW: https://ocw.mit.edu/courses/{slug}/\n")
        f.write(f"\n**Materials downloaded:** {ok} files (lecture notes typed+handwritten, problem sets, assessments+solutions, design project)\n")
        f.write("\n**Study order:** typed lecture notes -> handwritten notes (in-class) -> problem sets -> assessments (exams) -> design project\n")
        f.write("\n**Videos:** see videos.txt (YouTube)\n")
        if fail:
            f.write("\n**Failed:** " + ", ".join(fail) + "\n")
    with open(os.path.join(cdir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"course": "6.622", "title": title, "slug": slug, "files": len(links), "downloaded_ok": ok, "failed": fail}, f, indent=1)
    return ok

# ---------- part 2: videos.txt -> YouTube ----------
def fix_videos():
    changed, skipped = 0, []
    for track in ("software-engineering", "electrical-engineering"):
        tdir = os.path.join(ROOT, track)
        if not os.path.isdir(tdir):
            continue
        for d in sorted(os.listdir(tdir)):
            cdir = os.path.join(tdir, d)
            mpath = os.path.join(cdir, "manifest.json")
            if not os.path.isfile(mpath):
                continue
            meta = json.load(open(mpath, encoding="utf-8"))
            slug = meta.get("slug", "")
            if not slug:
                continue
            # find video gallery links on course page
            try:
                page_html = fetch(f"{BASE}/{slug}/").decode("utf-8", errors="ignore")
            except Exception:
                skipped.append(slug)
                continue
            galleries = re.findall(r'href="(/courses/' + re.escape(slug) + r'/video_galleries/[^"]+)"', page_html)
            galleries = sorted(set(galleries))
            entries = []  # (title, yt_url)
            for g in galleries:
                try:
                    gj = json.loads(fetch(BASE + g.replace("/video_galleries/", "/video_galleries/") + "data.json").decode("utf-8", errors="ignore"))
                    content = gj.get("content", "")
                    # parse video cards: img youtube thumb + h5 title + link
                    for m in re.finditer(r'<a class="video-link" href="([^"]+)">.*?<img class="thumbnail" src="https://img\.youtube\.com/vi/([^/]+)/.*?"[^>]*>\s*<h5 class="video-title">(.*?)</h5>', content, re.S):
                        vid = m.group(2)
                        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(3)))).strip()
                        entries.append((f"{title} — https://www.youtube.com/watch?v={vid}"))
                except Exception:
                    continue
            # fallback: search youtube ids in raw html/json
            if not entries:
                try:
                    gj = json.loads(fetch(f"{BASE}/{slug}/video_galleries/lecture-videos/data.json").decode("utf-8", errors="ignore"))
                    content = gj.get("content", "")
                    ids = re.findall(r"youtube\.com/vi/([A-Za-z0-9_-]{6,})", content)
                    titles = re.findall(r"video-title\">(.*?)</h5>", content, re.S)
                    titles = [re.sub(r"\s+", " ", html.unescape(t)).strip() for t in titles]
                    for i, vid in enumerate(ids):
                        t = titles[i] if i < len(titles) else f"Lecture {i+1}"
                        entries.append((f"{t} — https://www.youtube.com/watch?v={vid}"))
                except Exception:
                    pass
            if entries:
                with open(os.path.join(cdir, "videos.txt"), "w", encoding="utf-8") as f:
                    f.write(f"# {meta.get('course', slug)} | {meta.get('title', slug)} — lecture videos on YouTube\n")
                    f.write("# Stream online or download with: yt-dlp --batch-file videos.txt\n\n")
                    for line in entries:
                        f.write(line + "\n")
                changed += 1
                print(f"videos: {slug} -> {len(entries)} YouTube links")
            else:
                skipped.append(slug)
                print(f"videos: {slug} -> NO YouTube gallery found (kept archive.org links)")
    return changed, skipped

if __name__ == "__main__":
    ok622 = fix_6622()
    changed, skipped = fix_videos()
    print(f"\n6.622 files: {ok622}")
    print(f"videos.txt rewritten with YouTube: {changed} courses")
    print(f"no gallery found (archive.org kept): {skipped}")

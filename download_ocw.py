#!/usr/bin/env python3
"""Download MIT OCW course materials for the SE + EE curriculum.

For each course:
  1. Fetch the /download/ manifest page -> direct file URLs + video URLs
  2. Download all non-video resources (pdf, zip, code files)
  3. Organize into category folders (lecture-notes, assignments, exams, readings, software, other)
  4. Write README.md (description), syllabus.txt, videos.txt, manifest.json
"""
import json, os, re, sys, time, html, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"}

BASE = "https://ocw.mit.edu/courses"
OUT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mit-ocw-curriculum")

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

def strip_html(t):
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()

def strip_hash(name):
    m = re.match(r"^[0-9a-f]{32}_(.+)$", name)
    return m.group(1) if m else name

def categorize(name):
    n = name.lower()
    if re.search(r"\b(soln|solution|answer)\b", n):
        return "exams/solutions" if re.search(r"\b(exam|quiz|final|midterm|test)\b", n) else "assignments/solutions"
    if re.search(r"\b(lec|lecture|slides?|handout|note|notes)\b", n):
        return "lecture-notes"
    if re.search(r"\b(ps|problem|assignment|homework|hw|exercises?|lab)\b", n):
        return "assignments"
    if re.search(r"\b(exam|quiz|final|midterm|test)\b", n):
        return "exams"
    if re.search(r"\b(read|book|reference|manual)\b", n):
        return "readings"
    if n.endswith((".py", ".c", ".h", ".java", ".js", ".ipynb", ".m", ".ml")):
        return "software"
    if re.search(r"\b(install|code|software|tool)\b", n):
        return "software"
    return "other"

def get_meta(course_page_html):
    desc = ""
    m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', course_page_html)
    if m:
        desc = html.unescape(m.group(1))
    title = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", course_page_html, re.S)
    if m:
        title = strip_html(m.group(1))
    if not title:
        m = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', course_page_html)
        if m:
            title = html.unescape(m.group(1))
    return title, desc

def process_course(course):
    num, track, order, name, slug, _ = course
    cdir = os.path.join(OUT_ROOT, track, f"{order:02d}-{name}-{num}")
    os.makedirs(cdir, exist_ok=True)

    # 1. download page = manifest
    dl_html = fetch(f"{BASE}/{slug}/download/").decode("utf-8", errors="ignore")
    dl_url = re.escape(f"/courses/{slug}/")
    files = set()
    videos = []
    for m in re.finditer(r'href="([^"]+)"', dl_html):
        u = m.group(1)
        if re.match(rf"^{dl_url}[0-9a-f]{{32}}_", u):
            fname = strip_hash(u.split("/")[-1])
            ext = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
            if ext in ("mp4", "mov", "avi", "mkv", "webm"):
                videos.append("https://ocw.mit.edu" + u)
            elif ext in ("html", "xml", "json", "svg", "css", "js", "png", "jpg", "jpeg", "gif", "webp", "ico", "woff", "woff2", "ttf", "map", "md"):
                continue
            else:
                files.add((fname, "https://ocw.mit.edu" + u, u.split("/")[-1]))
    # video links from archive.org / youtube in the page
    for m in re.finditer(r'href="(https://archive\.org/download/[^"]+|https?://(?:www\.)?youtube\.com/[^"]+|https?://youtu\.be/[^"]+)"', dl_html):
        v = m.group(1)
        if v not in videos:
            videos.append(v)
    # also yt links with relative-absolute pattern
    for m in re.finditer(r'"contentUrl"\s*:\s*"([^"]+)"', dl_html):
        v = m.group(1)
        if "youtube" in v or "archive.org" in v:
            if v not in videos:
                videos.append(v)

    # 2. course page metadata
    title, desc = "", ""
    try:
        page_html = fetch(f"{BASE}/{slug}/").decode("utf-8", errors="ignore")
        title, desc = get_meta(page_html)
    except Exception:
        pass

    # 3. syllabus page -> text
    try:
        syl_html = fetch(f"{BASE}/{slug}/pages/syllabus/").decode("utf-8", errors="ignore")
        syl = strip_html(syl_html)
        syl = re.sub(r"\s{2,}", "\n", syl)
        with open(os.path.join(cdir, "syllabus.txt"), "w", encoding="utf-8") as f:
            f.write(f"{num} | {title or slug}\n{'=' * 60}\n\n" + syl)
    except Exception:
        pass

    # 4. download files
    dl_count = {"lecture-notes": 0, "assignments": 0, "assignments/solutions": 0, "exams": 0,
                "exams/solutions": 0, "readings": 0, "software": 0, "other": 0}
    ok, fail = 0, []
    manifest = []

    def dl_one(item):
        fname, url, raw = item
        cat = categorize(fname)
        dest = os.path.join(cdir, cat, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return fname, cat, "exists", 0
        try:
            data = fetch(url, timeout=120, retries=3)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as f:
                f.write(data)
            return fname, cat, "ok", len(data)
        except Exception as e:
            return fname, cat, f"ERR {type(e).__name__}", 0

    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(dl_one, it): it for it in files}
        for fut in as_completed(futs):
            fname, cat, status, size = fut.result()
            manifest.append({"file": fname, "category": cat, "status": status, "size": size})
            if status == "ok":
                ok += 1
                if cat in dl_count:
                    dl_count[cat] += 1
            elif status != "exists":
                fail.append(fname)

    # 5. videos.txt
    if videos:
        with open(os.path.join(cdir, "videos.txt"), "w", encoding="utf-8") as f:
            f.write(f"# {num} | {title or slug} - lecture videos (stream from archive.org / YouTube)\n")
            f.write("# Not downloaded to disk (large); play in browser or download with yt-dlp.\n\n")
            for v in sorted(set(videos)):
                f.write(v + "\n")

    # 6. README
    with open(os.path.join(cdir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {num} | {title or slug}\n\n")
        f.write(f"- MIT OCW: https://ocw.mit.edu/courses/{slug}/\n")
        f.write(f"- Download page: https://ocw.mit.edu/courses/{slug}/download/\n")
        if desc:
            f.write(f"\n**Description:** {desc}\n")
        f.write(f"**Materials downloaded:** {ok} files (see manifest.json)\n")
        f.write("**Contents:**\n")
        for k, v in dl_count.items():
            f.write(f"- {k}: {v}\n")
        f.write("\n**Study order:** 1) lecture-notes + videos.txt 2) assignments 3) exams (with solutions)\n")
        if "6.005" in meta.get("course", ""):
            f.write("\n**NOTE:** OCW hosts only quizzes for 6.005; the full Spring 2016 materials\n")
            f.write("(lectures, problem sets, code) live at the course site: https://web.mit.edu/6.005/www/fa16/\n")
        if fail:
            f.write("\n**Failed downloads:**\n")
            for x in fail:
                f.write(f"- {x}\n")

    with open(os.path.join(cdir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"course": num, "title": title, "slug": slug, "files": len(files),
                   "downloaded_ok": ok, "failed": fail, "videos": len(set(videos)),
                   "manifest": manifest}, f, indent=1)

    return {"course": num, "title": title, "files": len(files), "ok": ok, "fail": len(fail), "videos": len(set(videos))}

def main():
    courses = json.load(open(sys.argv[1], encoding="utf-8"))
    results = []
    for c in courses:
        try:
            r = process_course(c)
            print(f"OK  {c[0]:8s} {c[4][:55]:55s} files={r['files']:3d} ok={r['ok']:3d} fail={r['fail']} videos={r['videos']}")
            results.append(r)
        except Exception as e:
            print(f"ERR {c[0]:8s} {c[4][:55]:55s} {type(e).__name__}: {e}")
            results.append({"course": c[0], "error": str(e)})
    with open(os.path.join(OUT_ROOT, "download-summary.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    print("\nDONE. summary -> mit-ocw-curriculum/download-summary.json")

if __name__ == "__main__":
    main()

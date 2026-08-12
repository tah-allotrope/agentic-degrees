"""Workspace integrity checker for teach-workspace.

Verifies the file contract in the plan (## Specification §5):
- required workspace files exist
- lesson and learning-record numbering is contiguous from 0001 with no duplicates
- each lesson links the shared stylesheet, names a primary source, links back to
  MISSION.md, and contains a quiz section.

Standard library only. Run:
    python teach-workspace/tools/verify_workspace.py teach-workspace
"""

import argparse
import re
import sys
from pathlib import Path

LESSON_SUFFIX = ".html"
RECORD_SUFFIX = ".md"

REQUIRED_FILES = [
    "MISSION.md",
    "RESOURCES.md",
    "GLOSSARY.md",
    "NOTES.md",
    "PROGRESS.md",
    "LESSON-MAP.md",
    "assets/style.css",
    "assets/quiz.js",
]


def _name_re(suffix):
    return re.compile(r"^(\d{4})-[a-z0-9-]+" + re.escape(suffix) + r"$")


def scan_numbered(directory, suffix):
    """Return sorted (number, path) pairs for numbered files in `directory`.

    A file matches when its name is ^(\d{4})-[a-z0-9-]+<suffix>$. Returns [] when
    the directory does not exist. Non-matching names are silently ignored.
    """
    directory = Path(directory)
    if not directory.is_dir():
        return []
    pattern = _name_re(suffix)
    out = []
    for path in sorted(directory.iterdir()):
        match = pattern.match(path.name)
        if match:
            out.append((int(match.group(1)), path))
    return sorted(out)


def check_numbering(items, label):
    """Return problem strings for duplicate numbers and gaps from 0001.

    Returns [] when the sequence is contiguous from 1 or when `items` is empty.
    """
    problems = []
    numbers = set()
    for number, _ in items:
        if number in numbers:
            problems.append(f"{label}: duplicate number {number:04d}")
        numbers.add(number)
    if items:
        highest = max(n for n, _ in items)
        for n in range(1, highest + 1):
            if n not in numbers:
                problems.append(f"{label}: gap at {n:04d}")
    return problems


def check_lesson(path):
    """Return one problem string per missing required lesson element."""
    problems = []
    text = path.read_text(encoding="utf-8")
    if 'href="../assets/style.css"' not in text:
        problems.append(f"{path.name}: missing assets/style.css link")
    if "Primary source" not in text:
        problems.append(f"{path.name}: missing primary source")
    if 'href="../MISSION.md"' not in text:
        problems.append(f"{path.name}: missing mission link")
    if '<section class="quiz"' not in text:
        problems.append(f"{path.name}: missing quiz section")
    return problems


def check_required_files(workspace):
    """Return one problem string per missing required workspace file."""
    problems = []
    for name in REQUIRED_FILES:
        if not (Path(workspace) / name).is_file():
            problems.append(f"missing required file: {name}")
    return problems


def collect_problems(workspace):
    """Run all checks and return the concatenated problem list.

    Order: required files, lesson numbering, record numbering, per-lesson checks.
    """
    workspace = Path(workspace)
    problems = []
    problems.extend(check_required_files(workspace))
    lessons = scan_numbered(workspace / "lessons", LESSON_SUFFIX)
    records = scan_numbered(workspace / "learning-records", RECORD_SUFFIX)
    problems.extend(check_numbering(lessons, "lessons"))
    problems.extend(check_numbering(records, "records"))
    for _, lesson_path in lessons:
        problems.extend(check_lesson(lesson_path))
    return problems


def main(argv):
    parser = argparse.ArgumentParser(description="Verify a teaching workspace.")
    parser.add_argument(
        "workspace", nargs="?", default="teach-workspace",
        help="workspace directory to verify (default: teach-workspace)",
    )
    args = parser.parse_args(argv)

    workspace = Path(args.workspace)
    problems = collect_problems(workspace)
    lessons = scan_numbered(workspace / "lessons", LESSON_SUFFIX)
    records = scan_numbered(workspace / "learning-records", RECORD_SUFFIX)

    if not problems:
        print(f"OK: {len(lessons)} lessons, {len(records)} records, 0 problems")
        return 0
    for problem in problems:
        print(problem)
    print(f"FAIL: {len(problems)} problems")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

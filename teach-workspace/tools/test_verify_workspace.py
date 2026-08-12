"""Unit tests for verify_workspace.py.

Run:  python -m unittest discover -s teach-workspace/tools -p "test_*.py" -v
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from verify_workspace import (
    check_lesson,
    check_numbering,
    check_required_files,
    main,
    scan_numbered,
)

REQUIRED_WORKSPACE_FILES = [
    "MISSION.md",
    "RESOURCES.md",
    "GLOSSARY.md",
    "NOTES.md",
    "PROGRESS.md",
    "LESSON-MAP.md",
    "assets/style.css",
    "assets/quiz.js",
]

VALID_LESSON = """<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<p><a href="https://ocw.mit.edu">Primary source</a></p>
<p><a href="../MISSION.md">mission</a></p>
<section class="quiz">
<p>question?</p>
</section>
</body>
</html>
"""


class CheckNumberingTests(unittest.TestCase):
    def test_contiguous_sequence_ok(self):
        items = [(1, Path("0001-a.html")), (2, Path("0002-b.html"))]
        self.assertEqual(check_numbering(items, "lessons"), [])

    def test_gap_detected(self):
        items = [(1, Path("0001-a.html")), (3, Path("0003-c.html"))]
        self.assertEqual(check_numbering(items, "lessons"), ["lessons: gap at 0002"])

    def test_duplicate_detected(self):
        items = [(1, Path("0001-a.html")), (1, Path("0001-b.html"))]
        self.assertEqual(
            check_numbering(items, "lessons"), ["lessons: duplicate number 0001"]
        )

    def test_empty_items_ok(self):
        self.assertEqual(check_numbering([], "lessons"), [])

    def test_starting_at_two_reports_gap_at_one(self):
        items = [(2, Path("0002-a.html"))]
        self.assertEqual(check_numbering(items, "lessons"), ["lessons: gap at 0001"])


class ScanNumberedTests(unittest.TestCase):
    def test_ignores_non_matching_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "0001-x.html").touch()
            (directory / "notes.txt").write_text("not a lesson", encoding="utf-8")
            (directory / "0010-y.html").touch()
            result = scan_numbered(directory, ".html")
            self.assertEqual(
                result,
                [(1, directory / "0001-x.html"), (10, directory / "0010-y.html")],
            )

    def test_missing_directory_returns_empty(self):
        self.assertEqual(scan_numbered(Path("no-such-dir-xyz"), ".html"), [])


class CheckLessonTests(unittest.TestCase):
    def _write(self, content):
        path = Path(tempfile.mkdtemp()) / "0001-x.html"
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_lesson_ok(self):
        self.assertEqual(check_lesson(self._write(VALID_LESSON)), [])

    def test_missing_stylesheet_link(self):
        content = VALID_LESSON.replace('<link rel="stylesheet" href="../assets/style.css">', "")
        self.assertEqual(
            check_lesson(self._write(content)),
            ["0001-x.html: missing assets/style.css link"],
        )

    def test_missing_primary_source(self):
        content = VALID_LESSON.replace("Primary source", "First source")
        self.assertEqual(
            check_lesson(self._write(content)), ["0001-x.html: missing primary source"]
        )

    def test_missing_mission_link(self):
        content = VALID_LESSON.replace('href="../MISSION.md"', 'href="MISSION.md"')
        self.assertEqual(
            check_lesson(self._write(content)), ["0001-x.html: missing mission link"]
        )

    def test_missing_quiz_section(self):
        content = VALID_LESSON.replace('<section class="quiz">', "")
        self.assertEqual(
            check_lesson(self._write(content)), ["0001-x.html: missing quiz section"]
        )

    def test_multiple_missing_elements_reported(self):
        content = VALID_LESSON.replace('<link rel="stylesheet" href="../assets/style.css">', "")
        content = content.replace('<section class="quiz">', "")
        problems = check_lesson(self._write(content))
        self.assertIn("0001-x.html: missing assets/style.css link", problems)
        self.assertIn("0001-x.html: missing quiz section", problems)


class CheckRequiredFilesTests(unittest.TestCase):
    def test_missing_one_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            for name in REQUIRED_WORKSPACE_FILES:
                if name == "GLOSSARY.md":
                    continue
                path = workspace / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()
            self.assertEqual(
                check_required_files(workspace), ["missing required file: GLOSSARY.md"]
            )

    def test_all_present_ok(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            for name in REQUIRED_WORKSPACE_FILES:
                path = workspace / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()
            self.assertEqual(check_required_files(workspace), [])


def _make_valid_workspace(root):
    workspace = Path(root)
    (workspace / "lessons").mkdir()
    (workspace / "learning-records").mkdir()
    (workspace / "assets").mkdir()
    for name in REQUIRED_WORKSPACE_FILES:
        (workspace / name).touch()
    (workspace / "assets/style.css").write_text("body { }", encoding="utf-8")
    (workspace / "assets/quiz.js").write_text("", encoding="utf-8")
    (workspace / "lessons/0001-python-primer.html").write_text(
        VALID_LESSON, encoding="utf-8"
    )
    (workspace / "learning-records/0001-baseline.md").write_text(
        "# record", encoding="utf-8"
    )
    return workspace


class MainTests(unittest.TestCase):
    def test_valid_workspace_prints_ok(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = _make_valid_workspace(tmp)
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = main([str(workspace)])
            self.assertEqual(code, 0)
            self.assertTrue(buffer.getvalue().startswith("OK:"))

    def test_missing_notes_prints_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = _make_valid_workspace(tmp)
            (workspace / "NOTES.md").unlink()
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = main([str(workspace)])
            self.assertEqual(code, 1)
            self.assertTrue(buffer.getvalue().strip().endswith("FAIL:") or
                            buffer.getvalue().splitlines()[-1].startswith("FAIL:"))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import shutil
import sys
import unittest
from pathlib import Path
from uuid import uuid4

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_SOURCE = REPO_ROOT / "examples" / "minimal" / "source" / "acme" / "DESIGN.md"
EXAMPLE_BRANDS = REPO_ROOT / "examples" / "minimal" / "brands.txt"
TMP_ROOT = REPO_ROOT / ".tmp-tests"

sys.path.insert(0, str(REPO_ROOT / "src"))

from awesome_design_md_ppt_images.converter import convert_all, generate_ppt_image_design


class ConverterTests(unittest.TestCase):
    def test_generate_single_design_contains_expected_sections(self) -> None:
        output = generate_ppt_image_design(EXAMPLE_SOURCE, project_root=REPO_ROOT)
        self.assertIn("# PPT-image Design System Inspired by Acme", output)
        self.assertIn("## 9. Agent Prompt Guide", output)
        self.assertIn("presentation cover image", output)
        self.assertIn("Source reference: `examples/minimal/source/acme/DESIGN.md`", output)

    def test_convert_all_writes_manifest_and_placeholder(self) -> None:
        TMP_ROOT.mkdir(exist_ok=True)
        tmp_root = TMP_ROOT / f"case-{uuid4().hex}"
        tmp_root.mkdir(parents=True, exist_ok=True)
        try:
            source_root = tmp_root / "source"
            output_root = tmp_root / "out"
            manifest_path = tmp_root / "manifest.json"

            acme_dir = source_root / "acme"
            acme_dir.mkdir(parents=True)
            acme_dir.joinpath("DESIGN.md").write_text(EXAMPLE_SOURCE.read_text(encoding="utf-8"), encoding="utf-8")

            manifest = convert_all(
                source_root=source_root,
                output_root=output_root,
                manifest_path=manifest_path,
                brands_file=EXAMPLE_BRANDS,
                project_root=tmp_root,
            )

            self.assertEqual(manifest["repo_index_count"], 2)
            self.assertEqual(manifest["source_count"], 1)
            self.assertEqual(manifest["generated_count"], 1)
            self.assertEqual(manifest["missing_source_count"], 1)

            acme_output = output_root / "acme" / "DESIGN.md"
            ghost_output = output_root / "ghostco" / "DESIGN.md"
            self.assertTrue(acme_output.exists())
            self.assertTrue(ghost_output.exists())
            self.assertIn("PPT-image Design System Inspired by ghostco", ghost_output.read_text(encoding="utf-8"))

            manifest_on_disk = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest_on_disk["missing_sources"]["ghostco"], "Source DESIGN.md missing from the local source directory.")
        finally:
            shutil.rmtree(tmp_root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()

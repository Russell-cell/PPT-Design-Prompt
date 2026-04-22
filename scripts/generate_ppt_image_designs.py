from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from awesome_design_md_ppt_images.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main(["convert"], default_project_root=ROOT))

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from .converter import convert_all


def _date_arg(value: str) -> date:
    return date.fromisoformat(value)


def build_parser(default_project_root: Path) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="design-md-ppt",
        description="Convert DESIGN.md source files into presentation-image oriented DESIGN.md outputs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    convert = subparsers.add_parser("convert", help="Convert source DESIGN.md files into PPT-image DESIGN.md files.")
    convert.add_argument(
        "--source-root",
        type=Path,
        default=default_project_root / "source",
        help="Directory containing source/<brand>/DESIGN.md files.",
    )
    convert.add_argument(
        "--output-root",
        type=Path,
        default=default_project_root / "ppt-image",
        help="Directory where converted files will be written.",
    )
    convert.add_argument(
        "--manifest",
        type=Path,
        default=default_project_root / "conversion_manifest.json",
        help="Path for the generated manifest JSON.",
    )
    convert.add_argument(
        "--brands-file",
        type=Path,
        default=default_project_root / "catalog" / "brands.txt",
        help="Optional catalog of expected brand slugs. Missing brands receive placeholders.",
    )
    convert.add_argument(
        "--generated-on",
        type=_date_arg,
        default=None,
        help="Override the generation date in YYYY-MM-DD format.",
    )
    return parser


def main(argv: Sequence[str] | None = None, default_project_root: Path | None = None) -> int:
    project_root = (default_project_root or Path.cwd()).resolve()
    parser = build_parser(project_root)
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "convert":
        brands_file = args.brands_file if args.brands_file.exists() else None
        manifest = convert_all(
            source_root=args.source_root,
            output_root=args.output_root,
            manifest_path=args.manifest,
            brands_file=brands_file,
            generated_on=args.generated_on,
            project_root=project_root,
        )
        print(
            "Converted "
            f"{manifest['generated_count']} source files; "
            f"{manifest['missing_source_count']} placeholders; "
            f"manifest: {args.manifest}"
        )
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


#!/usr/bin/env python3
"""
Extract tag-based operation bundles from docs/openapi_md.json.

Creates one JSON file per OpenAPI tag with full operation details grouped under paths.

Usage:
  python scripts/extract_openapi_tags.py
  python scripts/extract_openapi_tags.py --input docs/openapi_md.json --output exported_tags
"""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "untitled_tag"


def load_json(path: Path) -> OrderedDict:
    with path.open("r", encoding="utf-8-sig") as fh:
        return json.load(fh, object_pairs_hook=OrderedDict)


def extract_by_tag(spec: OrderedDict) -> dict[str, OrderedDict]:
    by_tag: dict[str, OrderedDict] = {}
    paths = spec.get("paths", OrderedDict())

    for api_path, methods in paths.items():
        if not isinstance(methods, dict):
            continue

        for method, operation in methods.items():
            if not isinstance(operation, dict):
                continue

            tags = operation.get("tags") or ["untagged"]
            for tag_name in tags:
                tag_key = str(tag_name)
                if tag_key not in by_tag:
                    by_tag[tag_key] = OrderedDict()
                if api_path not in by_tag[tag_key]:
                    by_tag[tag_key][api_path] = OrderedDict()

                # Keep full operation object exactly as in source.
                by_tag[tag_key][api_path][method] = operation

    return by_tag


def get_tag_description(spec: OrderedDict, tag_name: str) -> str:
    for tag in spec.get("tags", []):
        if isinstance(tag, dict) and tag.get("name") == tag_name:
            return tag.get("description", "")
    return ""


def write_tag_files(spec: OrderedDict, by_tag: dict[str, OrderedDict], out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for tag_name in sorted(by_tag.keys(), key=lambda x: x.lower()):
        tag_paths = by_tag[tag_name]
        output = OrderedDict(
            [
                ("tag", tag_name),
                ("description", get_tag_description(spec, tag_name)),
                ("operationCount", sum(len(m) for m in tag_paths.values())),
                ("pathCount", len(tag_paths)),
                ("paths", tag_paths),
            ]
        )

        filename = f"{slugify(tag_name)}.json"
        file_path = out_dir / filename
        with file_path.open("w", encoding="utf-8") as fh:
            json.dump(output, fh, indent=2, ensure_ascii=False)
        written.append(file_path)

    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Split OpenAPI operations into one file per tag")
    parser.add_argument("--input", default="docs/openapi_md.json", help="Input OpenAPI JSON path")
    parser.add_argument("--output", default="exported_tags", help="Output folder for per-tag files")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    input_path = (project_root / args.input).resolve()
    output_dir = (project_root / args.output).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    spec = load_json(input_path)
    by_tag = extract_by_tag(spec)
    written = write_tag_files(spec, by_tag, output_dir)

    print(f"Input file : {input_path}")
    print(f"Output dir : {output_dir}")
    print(f"Tag files  : {len(written)}")
    for path in written:
        print(f" - {path.name}")


if __name__ == "__main__":
    main()

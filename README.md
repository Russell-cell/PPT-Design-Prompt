# PPT-Design-Prompt

Convert `DESIGN.md` brand references into presentation-image oriented
`DESIGN.md` files.

This repository is for **slide image systems**, not full slide decks, not HTML
presentations, and not product UI implementation. The goal is to turn web-first
brand guidance into a format that image models and design agents can use when
generating assets for PowerPoint, Keynote, PDF decks, or visual essays.

## What this repo is

- a converter from source `DESIGN.md` files to `ppt-image/<brand>/DESIGN.md`
- a small Python CLI that can be installed and re-run locally
- a generic presentation-image `DESIGN.md` at the repo root
- a minimal synthetic example for CI and contributor onboarding

## What this repo is not

- not a deck generator
- not a PowerPoint exporter
- not a screenshot scraper
- not a promise that every brand source can be legally redistributed

## Open-source boundary

This repository is structured so that **local downloaded sources stay local by
default**.

- `source/` is ignored by `.gitignore`
- the repository license applies to repo-authored code and docs
- third-party brand names and source materials remain the property of their
  owners
- if you publish converted brand outputs, review the legal notes in
  [ATTRIBUTION.md](./ATTRIBUTION.md)

If your local working copy already contains a populated `source/` directory,
double-check it before making an initial public commit.

## Repository layout

```text
.
+-- DESIGN.md                      # generic presentation-image design guide
+-- ATTRIBUTION.md                 # licensing and provenance boundary
+-- catalog/brands.txt             # optional expected brand catalog
+-- examples/minimal/              # synthetic example fixture
+-- ppt-image/                     # generated outputs
+-- scripts/                       # convenience wrapper for repo-local runs
+-- src/awesome_design_md_ppt_images/
|   +-- cli.py
|   +-- converter.py
+-- tests/
```

## Install

```bash
python -m pip install -e .
```

## Quick start

If you already have local source files under `source/<brand>/DESIGN.md`, run:

```bash
design-md-ppt convert
```

This writes:

- converted files to `./ppt-image`
- a manifest to `./conversion_manifest.json`

If you want explicit paths:

```bash
design-md-ppt convert \
  --source-root ./source \
  --output-root ./ppt-image \
  --manifest ./conversion_manifest.json \
  --brands-file ./catalog/brands.txt
```

## Example run without third-party data

This repo ships with a synthetic example so contributors can test the toolchain
without downloading live sources:

```bash
design-md-ppt convert \
  --source-root ./examples/minimal/source \
  --output-root ./examples/minimal/output \
  --manifest ./examples/minimal/manifest.json \
  --brands-file ./examples/minimal/brands.txt
```

## Legacy script

For people who prefer the old workflow, the repo still includes:

```bash
python ./scripts/generate_ppt_image_designs.py
```

That wrapper runs the same converter with repo-root defaults.

## Why the brand catalog exists

`catalog/brands.txt` is optional.

- if you provide it, the converter knows which brands are expected and can emit
  placeholders for missing sources
- if you omit it, the converter simply converts whatever exists under
  `source/`

This makes the tool self-contained and removes the old dependency on a sibling
`awesome-design-md_upstream` checkout.

## Development

Run tests:

```bash
python -m unittest discover -s tests -v
```

Run the example conversion:

```bash
design-md-ppt convert \
  --source-root ./examples/minimal/source \
  --output-root ./tmp-example-output \
  --manifest ./tmp-example-manifest.json \
  --brands-file ./examples/minimal/brands.txt
```

## Current repository state

This working tree currently contains generated outputs under `ppt-image/`. They
can be useful as a public catalog, but they may still be too close to upstream
brand materials for some maintainers' comfort level. If you want a stricter
open-source posture, keep the code and generic docs, then selectively review or
remove brand-specific generated outputs before your first public push.

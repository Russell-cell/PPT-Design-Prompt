# Attribution and Provenance

This repository contains three different kinds of material, and they do not all
share the same ownership or redistribution status.

## Repository-authored material

The following items are original to this repository unless otherwise noted:

- Python code under `src/`
- convenience scripts under `scripts/`
- tests, examples, and CI configuration
- the generic root-level `DESIGN.md`
- repository documentation such as `README.md` and `CONTRIBUTING.md`

These files are released under the repository's MIT license.

## Upstream inspiration and brand references

This project was created to work with the `DESIGN.md` ecosystem popularized by:

- `VoltAgent/awesome-design-md`
- the `getdesign` tooling and related live source pages

Brand names such as Apple, Anthropic / Claude, Figma, xAI, Stripe, and others
remain the property of their respective owners. This repository does not claim
endorsement by or affiliation with those brands.

## Local-only source material

The `source/` directory is intentionally ignored by `.gitignore`.

Why:

- those files may be downloaded from third-party sources at runtime
- redistribution rights may differ by source
- keeping them local reduces the chance of accidentally re-publishing upstream
  material that you do not own

If your local checkout already contains a populated `source/` directory, review
its contents before making an initial public commit.

## Generated brand conversions

Files under `ppt-image/<brand>/DESIGN.md` are transformed outputs produced by
this repository's converter. They are repo-generated artifacts, but they may be
derived from third-party source materials and brand systems.

Before publicly redistributing converted outputs:

- verify that you have the right to publish the underlying source material
- review the amount of direct quotation and brand-specific reference retained
- remove or rewrite files that are too close to the upstream originals for your
  risk tolerance

## Takedown

If you are a rights holder and believe a file in this repository should be
removed or rewritten, open an issue or contact the maintainer with the specific
path and rationale.


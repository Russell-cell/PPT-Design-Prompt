# Contributing

## Development setup

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Typical workflow

1. Put local source `DESIGN.md` files under `source/<brand>/DESIGN.md`
2. Run the converter:

```bash
design-md-ppt convert
```

3. Review the generated files under `ppt-image/`
4. Run tests before opening a pull request

## Please do

- keep changes small and reviewable
- add or update tests when behavior changes
- prefer repository-authored fixtures and examples over redistributing third-party
  source files
- document new CLI flags and behavior in `README.md`

## Please avoid

- committing `source/` unless you have verified redistribution rights
- adding machine-specific absolute paths to docs
- introducing unnecessary runtime dependencies


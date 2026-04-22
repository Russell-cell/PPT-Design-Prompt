# Examples

The repository ships with a small synthetic example under `examples/minimal/`.

It exists for two reasons:

- to show the expected source file shape without redistributing third-party data
- to give CI and contributors a stable fixture for local testing

Run the converter against the example:

```bash
design-md-ppt convert \
  --source-root ./examples/minimal/source \
  --output-root ./examples/minimal/output \
  --manifest ./examples/minimal/manifest.json \
  --brands-file ./examples/minimal/brands.txt
```


# Versioned reports

Reports are reviewed, curated research deliverables generated from one or more
immutable run IDs. They are committed by research question and report version.

```text
reports/<rq>/<report-version>/
  report.md
  report.yaml
  tables/
  figures/
  data/
  appendix/
```

Generated drafts stay under `outputs/report-build/` until reviewed.

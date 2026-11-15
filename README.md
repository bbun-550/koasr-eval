# koASR Eval

`koASR Eval` is a reproducible evaluation framework for Korean automatic
speech recognition (ASR). It separates inference, normalization, scoring,
statistical analysis, and curated reports so saved predictions can be
rescored without rerunning a model.

## Research roadmap

1. **RQ1** — Effects of evaluation unit and whitespace handling on model comparison
2. **RQ2** — Korean phonological errors and efficiency under quantization
3. **RQ3** — Confidence–CER calibration across domains

RQ1 is the first implementation target. RQ2 and RQ3 begin after the baseline
evaluation pipeline is stable.

## Repository layers

- `src/koasr_eval/`: reusable evaluation code
- `configs/`: versioned dataset, model, protocol, and experiment settings
- `schemas/`: machine-readable artifact contracts
- `docs/`: methods, guides, and versioned research protocols
- `outputs/`: generated local artifacts; contents are not committed
- `reports/`: reviewed and versioned research deliverables
- `tests/`: CPU unit, integration, and reproducibility tests

## Status

Initial scaffold. Public APIs and artifact schemas are not stable yet.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest
```

## Data policy

Raw audio, third-party datasets, model checkpoints, credentials, and
participant information are not committed. Dataset acquisition instructions,
checksums, and reproducible manifests are documented separately.

## License

Source code is licensed under the MIT License. Third-party datasets, models,
papers, and external materials remain subject to their own licenses.

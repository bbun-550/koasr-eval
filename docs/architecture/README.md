# Architecture

The pipeline is intentionally staged:

```text
dataset adapter -> manifest -> inference -> raw prediction
-> normalization -> scoring -> analysis -> curated report
```

Inference artifacts must remain independent from normalization and scoring so
normalizer changes do not require model reruns.

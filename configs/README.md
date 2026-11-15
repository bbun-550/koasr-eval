# Configurations

Committed inputs to reproducible experiments:

- `datasets/`: versions, splits, manifests, and sampling policies
- `models/`: model revisions, backends, precision, and decoding settings
- `protocols/`: versioned RQ-specific evaluation rules
- `experiments/`: runnable compositions of the above settings

Each run must save its resolved configuration under `outputs/runs/`.

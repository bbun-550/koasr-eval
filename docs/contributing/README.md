# Contributing

Changes to code, configuration, protocols, schemas, and reviewed reports use
the same short-lived branch and pull-request workflow. The goal is to keep
`main` reproducible at every commit, even while the public APIs are unstable.

## Set up and verify

Follow the [getting-started guide](../getting-started/README.md), then run:

```bash
make check
```

The local command and GitHub Actions run the same lint, CPU unit-test, and CLI
smoke-test gates. CI additionally verifies Python 3.10 and 3.12 against the
committed `uv.lock`.

## Branch model

Create each branch from the latest `main`. Do not use a long-lived `develop`
branch.

```bash
git switch main
git pull --ff-only origin main
git switch -c <type>/<short-topic>
```

Use one of these prefixes:

- `feat/` for evaluation, data-adapter, metric, or model functionality
- `fix/` for a reproducible defect
- `ci/` for automation and repository quality gates
- `build/` or `chore/` for dependencies and development tooling
- `docs/` for documentation-only changes

Include a WBS or research-question identifier when it helps trace the work,
for example `feat/wbs-1.3-dataset-zeroth` or `ci/wbs-1.2-quality-gates`.
Keep a branch limited to one reviewable outcome and merge it within one or two
work sessions when practical.

## Commits

Use an imperative Conventional Commit-style subject:

```text
feat: add manifest validator
fix: preserve empty hypothesis rows
ci: run locked checks across Python versions
docs: document dataset acquisition
```

Make commits atomic enough to review independently. Do not mix generated
outputs, unrelated formatting, or research results into an implementation
commit.

## Before pushing

```bash
git status --short
git diff --check
make check
```

Confirm that the diff contains no `.env` files, credentials, local absolute
paths, raw audio, dataset archives, model weights, or generated `outputs/`.
When dependencies change, run `uv lock`, review `uv.lock`, and commit it with
the corresponding `pyproject.toml` change.

## Pull requests

Open a draft pull request after the first push when the scope benefits from
early review. Complete the repository template with:

- the engineering or research reason for the change;
- what is intentionally outside the PR;
- exact validation commands and results;
- reproducibility effects;
- deferred work or known limitations.

Protocol and schema changes must update their version and changelog in the
same PR. Claims derived from experiments must reference an immutable run ID,
resolved config, code commit, and manifest rather than an untracked local
output.

## CI and merge

Both required checks must pass:

- `Python 3.10`
- `Python 3.12`

Resolve review conversations and update the branch with current `main` before
merging. Use squash merge so the PR becomes one logical commit on `main`, then
delete the remote topic branch. Direct pushes and force pushes to `main` are
not part of the normal workflow.

This is currently a single-maintainer repository, so required approvals may
remain at zero while status checks and the pull-request rule are enforced.
Increase required approvals to one when another maintainer joins.

## Research artifact boundaries

- Commit acquisition instructions, public metadata, checksums, and manifests.
- Do not commit third-party raw audio unless its license and the repository
  policy explicitly permit redistribution.
- Keep generated drafts under ignored output paths until provenance is
  validated and the reviewed artifact is intentionally promoted.
- Version normalization policies, scoring protocols, schemas, and report
  contracts so saved predictions can be rescored without ambiguity.

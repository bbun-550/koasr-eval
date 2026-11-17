# Getting started

This guide creates a reproducible local development environment and verifies
the repository scaffold. Dataset acquisition and model installation are
separate procedures and are not required here.

## Prerequisites

- Git
- GNU Make
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- network access for the first Python and dependency download

Do not add API tokens to shell history or tracked files. Copy `.env.example`
to `.env` only when a later workflow requires credentials; `.env` is ignored.

## Clone and install

```bash
git clone git@github.com:bbun-550/koasr-eval.git
cd koasr-eval
make setup
```

`make setup` asks uv to install the reference Python 3.12 interpreter and
syncs the locked development environment into `.venv`. It does not install
packages into the macOS or Linux system Python.

The lockfile is authoritative. If `make setup` reports that `uv.lock` is out
of date, do not bypass `--locked`: update the declared dependencies in
`pyproject.toml`, run `uv lock`, review the lockfile diff, and commit both
files in the same pull request.

## Verify

```bash
make check
```

This runs, in order:

1. `ruff check .`
2. the CPU pytest suite
3. `koasr-eval --help` as a CLI smoke test

The commands can also be run separately:

```bash
make lint
make test
make smoke
```

A successful setup must leave `git status --short` empty. `.venv`, caches,
credentials, raw audio, model weights, and generated run outputs must remain
untracked.

## Supported Python versions

The package metadata supports Python 3.10 through 3.12. Python 3.12 is the
reference local version selected by `.python-version`; CI is responsible for
the lower-version compatibility checks.

## Troubleshooting

### The system Python is older than 3.10

Run `make setup`. uv installs and selects Python 3.12 for this project, so the
system Python version is not used.

### `uv` or `make` is not found

Install the missing prerequisite and restart the shell so its executable is
on `PATH`. Do not replace the locked workflow with an unrecorded global pip
installation.

### Dependency resolution changes unexpectedly

Confirm that the current branch intentionally changes `pyproject.toml`. A
normal clone should use `make setup`, which refuses to rewrite `uv.lock`.

## Cleaning local tool caches

```bash
make clean
```

This removes only the repository-local pytest, ruff, build, and distribution
caches named in the Makefile. It does not remove `.venv`, datasets, models,
or experiment outputs.

"""Command-line entry point for koASR Eval."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level command-line parser."""
    parser = argparse.ArgumentParser(
        prog="koasr-eval",
        description="Reproducible, normalization-aware evaluation for Korean ASR.",
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    return parser


def main() -> int:
    """Run the command-line interface."""
    build_parser().parse_args()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

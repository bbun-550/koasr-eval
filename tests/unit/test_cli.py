import pytest

from koasr_eval.cli import build_parser


def test_cli_program_name() -> None:
    assert build_parser().prog == "koasr-eval"


def test_cli_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        build_parser().parse_args(["--version"])

    assert exc_info.value.code == 0
    assert capsys.readouterr().out == "koasr-eval 0.1.0\n"

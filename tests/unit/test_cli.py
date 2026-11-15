from koasr_eval.cli import build_parser


def test_cli_program_name() -> None:
    assert build_parser().prog == "koasr-eval"

import argparse

from unattended_mode.cli import add_unattended_cli_options, parse_unattended_args


def test_add_unattended_cli_options():
    parser = argparse.ArgumentParser()
    add_unattended_cli_options(parser)
    args = parser.parse_args(['--quiet', '--no-log', '--daemon', '--log-file', 'test.log'])

    assert args.quiet is True
    assert args.no_log is True
    assert args.daemon is True
    assert args.log_file == 'test.log'


def test_parse_unattended_args():
    args = parse_unattended_args(['--quiet', '--log-file', 'output.log'])
    assert args.quiet is True
    assert args.no_log is False
    assert args.log_file == 'output.log'

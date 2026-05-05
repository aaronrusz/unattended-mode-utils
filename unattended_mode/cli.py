import argparse
from argparse import ArgumentParser


def add_unattended_cli_options(parser: ArgumentParser) -> ArgumentParser:
    """Add unattended-mode CLI options to an argument parser."""
    parser.add_argument('--quiet', action='store_true', help='Suppress console output')
    parser.add_argument('--no-log', action='store_true', help='Disable logging to file')
    parser.add_argument('--log-file', type=str, default='unattended_mode.log', help='Path to log file')
    parser.add_argument('--daemon', action='store_true', help='Run as a background daemon process')
    return parser


def parse_unattended_args(args=None):
    """Parse unattended CLI arguments and return the parsed namespace."""
    parser = argparse.ArgumentParser(description='Unattended mode options')
    add_unattended_cli_options(parser)
    return parser.parse_args(args)

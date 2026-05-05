# Unattended Mode Utils

Reusable utilities for running Python scripts in unattended mode with quiet output, optional file logging, and optional daemon/background execution.

## Features

- `configure_unattended_logging(...)`
- `daemonize_process()`
- `redirect_std_streams()`
- `add_unattended_cli_options(parser)`

## Installation

```bash
pip install unattended-mode-utils
```

## Usage

```python
import argparse
from unattended_mode import (
    add_unattended_cli_options,
    configure_unattended_logging,
    daemonize_process,
    redirect_std_streams,
)


def main():
    parser = argparse.ArgumentParser(description='Example unattended script')
    add_unattended_cli_options(parser)
    args = parser.parse_args()

    configure_unattended_logging(
        quiet=args.quiet,
        no_log=args.no_log,
        log_file=args.log_file,
    )

    if args.daemon:
        daemonize_process()
        redirect_std_streams()

    # Replace with your script logic
    print('Running unattended script')


if __name__ == '__main__':
    main()
```

## Notes

- This library suppresses console interaction and logging output when requested.
- It does not make a process undetectable at the OS or network level.

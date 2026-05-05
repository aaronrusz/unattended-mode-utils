import os
import sys


def daemonize_process() -> None:
    """Daemonize the current process.

    This uses a standard double-fork pattern to detach from the controlling terminal.
    """
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as exc:
        raise RuntimeError(f'Failed to daemonize (first fork): {exc}') from exc

    os.setsid()

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as exc:
        raise RuntimeError(f'Failed to daemonize (second fork): {exc}') from exc

    sys.stdout.flush()
    sys.stderr.flush()

    with open(os.devnull, 'rb', 0) as stdin, open(os.devnull, 'ab', 0) as stdout, open(os.devnull, 'ab', 0) as stderr:
        os.dup2(stdin.fileno(), sys.stdin.fileno())
        os.dup2(stdout.fileno(), sys.stdout.fileno())
        os.dup2(stderr.fileno(), sys.stderr.fileno())


def redirect_std_streams() -> None:
    """Redirect stdout and stderr to /dev/null."""
    with open(os.devnull, 'wb', 0) as devnull:
        os.dup2(devnull.fileno(), sys.stdout.fileno())
        os.dup2(devnull.fileno(), sys.stderr.fileno())

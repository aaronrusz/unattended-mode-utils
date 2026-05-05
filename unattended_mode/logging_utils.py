import logging


def configure_unattended_logging(quiet: bool = False, no_log: bool = False, log_file: str = 'unattended_mode.log') -> None:
    """Configure logging for unattended execution.

    Parameters:
        quiet: If True, suppress console output.
        no_log: If True, disable file logging.
        log_file: File path to write logs when logging is enabled.
    """
    handlers = []

    if not no_log:
        handlers.append(logging.FileHandler(log_file))

    if not quiet:
        handlers.append(logging.StreamHandler())

    if handlers:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=handlers,
        )
    else:
        logging.disable(logging.CRITICAL)

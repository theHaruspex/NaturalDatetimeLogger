from .setup import initialize_logging

logger = initialize_logging(log_file="20.03_test", level=logging.DEBUG)

logger.info("This is an informational log entry.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")

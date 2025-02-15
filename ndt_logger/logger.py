# utils/custom_logging/setup.py

from .formatter import NaturalLanguageFormatter

def initialize_logging(log_dir="logs", log_file="app.log", enable_debug_file=False):
    import logging, os

    # Make sure directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Use the filename (or a unique name) as the logger's name
    logger = logging.getLogger(log_file)  # named logger, not root

    # Avoid re-adding handlers if logger already exists
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)  # to capture all logs

    main_log_path = os.path.join(log_dir, log_file)
    main_file_handler = logging.FileHandler(main_log_path)
    main_file_handler.setLevel(logging.INFO)

    # (Optional) debug file
    if enable_debug_file:
        base, ext = os.path.splitext(log_file)
        debug_log_file = f"{base}_debug{ext}"
        debug_file_handler = logging.FileHandler(os.path.join(log_dir, debug_log_file))
        debug_file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Custom formatter
    formatter = NaturalLanguageFormatter(fmt="%(asctime)s - %(levelname)s - %(message)s")
    main_file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(main_file_handler)
    logger.addHandler(console_handler)

    if enable_debug_file:
        debug_file_handler.setFormatter(formatter)
        logger.addHandler(debug_file_handler)

    logger.propagate = False
    return logger
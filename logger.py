import logging
import os


def setup_logger(log_filename="request.log"):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        os.path.join("logs", log_filename), encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[%(levelname)s][%(asctime)s][%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

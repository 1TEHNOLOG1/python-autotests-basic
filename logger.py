import logging


def setup_logger(log_filename='request.log'):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_filename)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S,%f')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

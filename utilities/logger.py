import logging

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("reports/test.log")
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))
        logger.addHandler(handler)
    return logger

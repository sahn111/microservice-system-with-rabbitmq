"""
This is the file that will contain all other logging functions except notification sending process

- request logging

- response logging

- exception logging

"""
from logging.handlers import RotatingFileHandler

import logging
import os

def __init_logger():
    """
    This will start logging file is it not exist, or it will retrun logger
    """
    directory = "consumer_app/log_files/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    path_to_file = f"{directory}system.log"
    logger = logging.getLogger('consumer_system_logger')
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = RotatingFileHandler(path_to_file, maxBytes=1000000000, backupCount=5)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def start_logging() -> None:
    return __init_logger()
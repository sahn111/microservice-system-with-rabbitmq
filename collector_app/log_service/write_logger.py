from .start_logger import start_logging

from ..schema import SystemLogPydantic

def write_system_logging_message(log : SystemLogPydantic) -> None:
    logger = start_logging()

    if log.type == "CRITICAL":
        logger.critical(log.message)
    elif log.type == "WARNING":
        logger.warning(log.message)
    elif log.type == "ERROR":
        logger.error(log.message)
    elif log.type == "INFO":
        logger.info(log.message)
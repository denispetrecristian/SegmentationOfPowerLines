import logging
import os
import datetime

class Logger():
    def __init__(self, model:str) -> None:
        path = os.path + f'/logs/{model}'
        logging.basicConfig(f'{path}/{str(datetime.date)}')

    def log(message:str, log_level: int):
        match log_level:
            case logging.DEBUG:
                logging.debug(message)
            case logging.ERROR:
                logging.error(message)
            case logging.INFO:
                logging.info(message)
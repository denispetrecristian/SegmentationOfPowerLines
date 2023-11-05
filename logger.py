import logging
import os
import datetime
import pathlib

class Logger():
    def __init__(self, model:str) -> None:
        now = datetime.datetime.now()
        # Get the directory path

        path_cwd = str(pathlib.Path().resolve()) + f'/logs/{model}'
        filepath = f'{path_cwd}/{model}-{str(now.month)}-{str(now.day)}.txt'
        logging.basicConfig(filename=filepath, force=True)

    def log(self,message:str, log_level: int):
        match log_level:
            case logging.DEBUG:
                logging.debug(message)
            case logging.ERROR:
                logging.error(message)
            case logging.INFO:
                logging.info(message)
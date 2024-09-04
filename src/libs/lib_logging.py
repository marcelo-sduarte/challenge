from gvars import PATH_LOGS,FILENAME
import logging, os


def create_logger():
    
    if not os.path.isdir(PATH_LOGS):
        os.mkdir(PATH_LOGS)
   
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'a'): 
            pass

    # create Logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # create console handler and set level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler and set level
    fh = logging.FileHandler(
        filename=FILENAME, 
        mode="a", 
        encoding="utf-8"
    )
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - {%(filename)s:%(lineno)d} - %(message)s", 
        datefmt="%d-%m-%y %H:%M:%S %p"
    )

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to Logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

# set logger global variable
global logger
logger = create_logger()

if __name__ == "__main__":
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
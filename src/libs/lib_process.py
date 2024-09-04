import pieces
from gvars import *

def verify_structure():
    if not pieces.os.path.exists(PATH_INPUT):
        pieces.os.mkdir(PATH_INPUT)
    if not pieces.os.path.exists(PATH_OUTPUT):
        pieces.os.mkdir(PATH_OUTPUT)
    if not pieces.os.path.exists(PATH_LOGS):
        pieces.os.mkdir(PATH_LOGS)
    if not pieces.os.path.exists(PATH_FILES):
        pieces.os.mkdir(PATH_FILES)    
   # if not pieces.os.path.exists(PATH_CHROMEDRIVER):
   #     pieces.os.mkdir(PATH_CHROMEDRIVER) 
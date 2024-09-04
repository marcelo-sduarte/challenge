import pieces

# PROCESS
PROCESS_NAME = "extract_data_ibge"

# paths
PATH_PROCESS_FOLDER = fr"C:\Users\Documents\Python\Automation"+ pieces.os.sep + PROCESS_NAME
PATH_OUTPUT = PATH_PROCESS_FOLDER + pieces.os.sep + "output"
PATH_INPUT = PATH_PROCESS_FOLDER + pieces.os.sep + "input"
PATH_LOGS = PATH_OUTPUT + pieces.os.sep +"logs"
PATH_FILES = PATH_OUTPUT + pieces.os.sep +"files"

CHROMEDRIVER = PATH_PROCESS_FOLDER + pieces.os.sep + "src\chromedriver\chromedriver.exe"
PATH_CHROMEDRIVER = fr"{PATH_PROCESS_FOLDER}\src\chromedriver"

# TODAY
HOJE = pieces.date.today().strftime('%d-%m-%yyyy') 

TODAY = pieces.date.today()

PATH_ID_CHROMEDRIVER = fr"{PATH_CHROMEDRIVER}\id_chrome.json"

#filename logs
FILENAME = PATH_LOGS + pieces.os.sep + fr"output-{HOJE}.log"

# URL
URL = "https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html"

#BROWSER LIST
BROWSERS = ["CHROME","FIREFOX"]

#DATABASE
DATABASE = ""
USER = ""
PASSWORD = ""
PORT = "3306"
HOST = "127.0.0.1"


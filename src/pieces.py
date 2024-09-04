import os
from datetime import date, datetime
from enum import Enum
import json
import mysql.connector
from mysql.connector import Error
from libs import lib_browserdriver, lib_ibge, lib_process,lib_logging,lib_mysql
from libs.lib_logging import logger
from libs.lib_browserdriver import EnumCommand, EnumWindowHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import shutil
from fake_useragent import UserAgent



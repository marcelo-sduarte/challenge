import pieces
from gvars import PATH_ID_CHROMEDRIVER, PATH_PROCESS_FOLDER,PATH_CHROMEDRIVER,CHROMEDRIVER, URL, BROWSERS, PATH_FILES


class EnumCommand(pieces.Enum):
    """[Is used to Specify the type of Command will be used]\n
        CLICK = 1\n
        WRITE = 2\n
        GET_TEXT = 3\n
        CLEAR = 4\n
        GET_ELEMENT = 5\n
        GET_ELEMENTS = 6\n
        MOVE_TO = 7\n
        SELECT_OPTION = 8\n
    """
    CLICK = 1
    WRITE = 2
    GET_TEXT = 3
    CLEAR = 4
    GET_ELEMENT = 5
    GET_ELEMENTS = 6
    MOVE_TO = 7
    SELECT_OPTION = 8
    ACTION_CHAIN = 9
    RIGHT_CLICK = 10
    ENTER = 11


class EnumWindowHandler(pieces.Enum):
    """[Is used to Specify the type of Command will be used]\n
        NAVIGATE = 1\n
        NAVIGATE_BACK = 2\n
        NAVIGATE_FORWARD = 3\n
        REFRESH = 4\n
        SWITCH_TAB = 5\n
        QUIT = 6\n
    """
    NAVIGATE = 1
    NAVIGATE_BACK = 2
    NAVIGATE_FORWARD = 3
    REFRESH = 4
    SWITCH_TAB = 5
    QUIT = 6


def abrir_browser(hide=False, cookie=False, browser=None):
    
    """
    Função abrir_navegador:
    
    Entrada:
        
    Retornos: 
        driver   # Sucesso ao abrir_navegador
    """
    if browser == None or browser.upper() not in BROWSERS:
        pieces.logger.info(f" Navegador[{browser}] não permitido, continuando no Chrome")
        browser ="CHROME"
        chrome = True
    if browser.upper() == "CHROME":
        chrome = True
    else:
        chrome = False

                
    

    pieces.logger.info(f"[INICIO] abrir navegador:[{browser}]")
    
    global driver
    pieces.logger.info("Iniciando instância do navegador configurado...")
    ua = pieces.UserAgent()
    userAgent = ua.random
    # Configurar opções do Chrome
    chrome_options = pieces.webdriver.ChromeOptions()            
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--lang=pt-BR')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-cookies")
    chrome_options.add_argument("--disable-local-storage")

    # Configurar as opções do Firefox
    firefox_options = pieces.Options()
    firefox_options.set_preference("intl.accept_languages", "pt-BR")  # Definir o idioma para pt-BR
    firefox_options.add_argument('--disable-infobars')  # Desativar barras de informação
    firefox_options.add_argument('--log-level=3')  # Definir o nível de log
    # As opções '--no-sandbox' e '--disable-gpu' são específicas para o Chrome e não se aplicam ao Firefox
    scriptDirectory = PATH_PROCESS_FOLDER
    if cookie:
        chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
        firefox_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
    if hide:
        chrome_options.add_argument('--headless')
        firefox_options.add_argument('--headless')
    # Definir preferências do navegador
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "download.default_directory": PATH_FILES,  
        "download.prompt_for_download": False,  
        "download.directory_upgrade": True,  
        "safebrowsing.enabled": True  
    }
    pieces.logger.info(f"path files...{PATH_FILES}")
    # Excluir switches específicos
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])            
    
    # Configurar o ChromeDriver automaticamente usando o webdriver-manager
    #driver = pieces.webdriver.Chrome(service=pieces.ChromeDriverManager().install())
    
    if chrome:
        #usando Chrome
        service = pieces.Service(pieces.ChromeDriverManager().install())
        driver = pieces.webdriver.Chrome(service=service)
    else:
        #usando firefox
        service = pieces.FirefoxService(pieces.GeckoDriverManager().install())
        driver = pieces.webdriver.Firefox(service=service, options=firefox_options)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    
    url = str(executor_url) + " " + str(session_id)
    pieces.logger.info(f"url: {url}")
    
    chrome = False

    return driver


def attach_to_session(executor_url, session_id, implicity_wait=0):
    try:
        pieces.logger.info("Criando webdriver Remote...")
        driver = pieces.webdriver.Remote(
            command_executor=executor_url, 
            desired_capabilities={}
        )
        
        driver.close()
        driver.session_id = session_id        
        driver.implicitly_wait(implicity_wait) # seconds
        
        pieces.logger.info("Retornando driver...")
        return driver
    except Exception as error:
        pieces.logger.info(f"attach_to_session error -> {error}")
        pass


def wait_execute_script(*, driver, script, timeout = 30):
    """
    Entradas:
        driver (obj) : Instância do chrome
        script (str) : script a ser executado
        timeout (int) : tentar executar por quanto tempo?
    """
    
    # se o script nao tiver retorno, 
    if script[:6] != "return":
        # pieces.logger.info(f"Script não tinha 'return', adicionando!")
        script = f"return {script}"
        
    # salva a hora que começou o loop
    time_begin = int(round(pieces.time.time() * 1000))
    while True: #loop infinito
        time_now = int(round(pieces.time.time() * 1000))
        if (time_now - time_begin) / 1000 >= timeout:
            pieces.logger.info(f"timeout executando script após {(time_now - time_begin)/1000} segundos")
            return -1
            
        try:
            r = driver.execute_script(script)
            r = 1 if r is None else r
            return r
        except:
            pieces.time.sleep(1)


def wait_ready_state(*, driver, timeout = 60) :
    '''
    Descrição:
        Função para verificar o Ready State da página
    Inputs:
        driver (obj)          : Objeto do ChromeDriver
        pieces.timeout (int)         : Segundpieces.os para pieces.timeOut
    Outputs:
         1 (int) : Retorno bem sucedido
        -1 (int) : Erro
    '''
    ind_timeout = 0
    element_founded = False
    ready_state = ""
    
    while ind_timeout <= timeout and element_founded != True:
        try:
            ready_state = driver.execute_script("return document.readyState")
            if ready_state == "complete" :
                element_founded = True
        except:
            pieces.time.sleep(1)
            ind_timeout += 1

    if ind_timeout > timeout :
        pieces.logger.info("timeout ao esperar carregamento do browser")
        return -1

    return 1


def action(driver, command : EnumCommand, xpath, text='', wait_until=5, wait_before_find_sec=0, wait_after_find_sec=0, wait_after_interaction_sec=0):
    """
        Method of actions for selenium interaction, it needs the import of EnumCommand enum

        Parameters:\n
            command (EnumCommand): The action selenium will perform
            xpath (string): Location of the Element
            text (string): Content that will be written
            wait_until (int): Wait in sec For element to show, default: 20
            wait_before_find_sec (int): Wait before element is shown, default: 0
            wait_after_find_sec (int): Wait after the element is shown, default: 0
            wait_after_interaction (int): Wait after the interaction with the element, default: 0
    """
    pieces.WebDriverWait(driver, wait_until)
    pieces.time.sleep(wait_before_find_sec)

    if command != EnumCommand.GET_ELEMENTS and command != EnumCommand.ACTION_CHAIN:
        element = pieces.WebDriverWait(driver, wait_until).until(pieces.EC.presence_of_element_located((pieces.By.XPATH, xpath)))
        pieces.time.sleep(wait_after_find_sec)

    if command is EnumCommand.CLICK:
        element.click()
    elif command is EnumCommand.WRITE:
        element.send_keys(text)
    elif command is EnumCommand.GET_TEXT:
        if element.text:
            return element.text
        else:
            return element.get_attribute('value')
    elif command is EnumCommand.CLEAR:
        element.clear()
    elif command is EnumCommand.GET_ELEMENT:
        return element
    elif command is EnumCommand.GET_ELEMENTS:
        return driver.find_elements(pieces.By.XPATH, xpath)
    elif command is EnumCommand.MOVE_TO:
        actions = pieces.ActionChains(driver)
        actions.move_to_element(element).perform()
    elif command is EnumCommand.SELECT_OPTION:
        pieces.Select(element).select_by_value(text)
    elif command is EnumCommand.ACTION_CHAIN:
        actions = pieces.ActionChains(driver)
        actions.send_keys(text).perform()
    elif command is EnumCommand.RIGHT_CLICK:
        action = pieces.ActionChains(driver)
        action.context_click(element).perform()
    elif command is EnumCommand.ENTER:
        actions = pieces.ActionChains(driver)
        actions.send_keys(pieces.Keys.ENTER).perform()

    pieces.time.sleep(wait_after_interaction_sec)


def window_action(*, driver, command: EnumWindowHandler, url = ''):
    """
        Method of actions for window manipulation, it needs the import of EnumWindowHandler enum

        Parameters:\n
            command (EnumWindowHandler): The action window will perform\n
            url (string): Only if you will go to another url\n
    """
    if command is EnumWindowHandler.NAVIGATE:
        driver.get(url)
    elif command is EnumWindowHandler.NAVIGATE_BACK:
        driver.back()
    elif command is EnumWindowHandler.NAVIGATE_FORWARD:
        driver.forward()
    elif command is EnumWindowHandler.REFRESH:
        driver.refresh()
    elif command is EnumWindowHandler.QUIT:
        pieces.time.sleep(2)
        driver.close()
        driver.quit()


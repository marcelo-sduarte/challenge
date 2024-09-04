import pieces
from gvars import URL
def get_file_ibge(nomeBrowser):
    driver = pieces.lib_browserdriver.abrir_browser(browser=nomeBrowser)

    try:
        pieces.logger.info(f" [INICIO] abre_url() -> {URL}")
        pieces.lib_browserdriver.window_action(driver=driver, command=pieces.EnumWindowHandler.NAVIGATE, url= URL)    
        driver.maximize_window()
    except Exception as error:
        msg_erro = f'Erro navegando para url -> {URL}, erro message:{error}'
        pieces.logger.info(msg_erro)

        return {
            'code' : -1,
            'message' : msg_erro
        }
    finally:
        pieces.logger.info(f" [FIM] abre_url() -> {URL}")
    try:
        pieces.logger.info(f" fechando banner()")
        str_xpath = "//*[normalize-space(text())='PROSSEGUIR']"
        pieces.lib_browserdriver.action(driver=driver, command=pieces.EnumCommand.CLICK, xpath=str_xpath, wait_before_find_sec=5)
    except:
        pass

    try:
        pieces.logger.info(f" [INICIO] navega_menu()")
        str_xpath = "//*[@id='Censos']/div"
        pieces.logger.info(f" Clica Censo")
        pieces.lib_browserdriver.action(driver=driver, command=pieces.EnumCommand.CLICK, xpath=str_xpath, wait_before_find_sec=10)
    except Exception as error:
        msg_erro = f'Erro clicando xpath:[{str_xpath}],{error}'
        pieces.logger.info(msg_erro)
        return {
            'code' : -2,
            'message' : msg_erro
        }
    
    try:
        str_xpath = "//*[@id='Censos/Censo_Demografico_1991_anchor']"
        pieces.logger.info(f" Clica no Censo_Demografico_1991")
        pieces.lib_browserdriver.action(driver=driver, command=pieces.EnumCommand.CLICK, xpath=str_xpath, wait_before_find_sec=2)
    except Exception as error:
        msg_erro = f'Erro clicando xpath:[{str_xpath}],{error}'
        pieces.logger.info(msg_erro)
        return {
            'code' : -3,
            'message' : msg_erro
        }
    
    try:   
        str_xpath = "//*[@id='Censos/Censo_Demografico_1991/Indice_de_Gini_anchor']"
        pieces.logger.info(f" Clica no Indice_de_Gini")
        pieces.lib_browserdriver.action(driver=driver, command=pieces.EnumCommand.CLICK, xpath=str_xpath, wait_before_find_sec=3)
    except Exception as error:
        msg_erro = f'Erro clicando xpath:[{str_xpath}],{error}'
        pieces.logger.info(msg_erro)
        return {
            'code' : -4,
            'message' : msg_erro
             }
    try:   
        str_xpath = "//*[@id='Censos/Censo_Demografico_1991/Indice_de_Gini']/ul/li"
        pieces.logger.info(f" Recupera total de files")
        elements = pieces.lib_browserdriver.action(driver=driver, command=pieces.EnumCommand.GET_ELEMENTS, xpath=str_xpath, wait_before_find_sec=3)
        pieces.logger.info(f"Total de elementos: {len(elements)}")
    except Exception as error:
        msg_erro = f'Erro clicando xpath:[{str_xpath}],{error}'
        pieces.logger.info(msg_erro)
        return {
            'code' : -5,
            'message' : msg_erro
             }
    try:        
        pieces.logger.info(f" Extraindo files -> {URL}")
        lista_anexos = []
        for element in elements:
            text = element.text 
            txt = text.strip()
            str_xpath = f"//*[normalize-space(text())='{txt}']"
            if text:
                pieces.logger.info(f"clicando no xpath: [{str_xpath}]")
                pieces.lib_browserdriver.action(driver=driver, command=pieces.EnumCommand.CLICK, xpath=str_xpath, wait_after_interaction_sec=1)                                
                lista_anexos.append(txt)
                #break
    except Exception as error:
        msg_erro = f'Erro clicando xpath:[{str_xpath}],{error}'
        pieces.logger.info(msg_erro)
        return {
            'code' : -6,
            'message' : msg_erro
             }
            
    try:        
        pieces.logger.info(f" Fechando navegador...")
        pieces.lib_browserdriver.window_action(driver=driver, command=pieces.EnumWindowHandler.QUIT)
    except Exception as error:
        msg_erro = f'Erro fechando navegador:[{str_xpath}],{error}'
        pieces.logger.info(msg_erro)
        return {
            'code' : -7,
            'message' : msg_erro
             }
     try:
        for file_name in lista_anexos:
            file_path = pieces.os.path.join(PATH_DOWNLOAD, file_name)
            if pieces.os.path.isfile(file_path):
                destination_path = pieces.os.path.join(PATH_FILES, file_name)
                pieces.shutil.move(file_path, destination_path)
                pieces.logger.info(f'Movendo arquivo: {file_path} para {PATH_FILES}')
                
    except Exception as error:
        pieces.logger.info(msg_erro)
        return {
            'code' : -8,
            'message' : msg_erro
             }      
    pieces.logger.info(f" [FIM] navega_menu() -> {URL}")
    return {
            'code' : 0,
            'message' : 'Executou com sucesso!',
            'lista' : lista_anexos
             }
    
    
    


    
    

    
    

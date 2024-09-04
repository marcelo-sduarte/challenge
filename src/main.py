import pieces

def start_process():
    try:
        status_process = False
        pieces.logger.info(f" [INICIO] start_process()")
        # Verifica o framework de pastas da automatizacao
        pieces.lib_process.verify_structure()

        # Inicia o processo de conexao e extracao de files do site
        status = pieces.lib_ibge.get_file_ibge(nomeBrowser="CHROME")

        # Inicia o processo de conexao e atualizacao das informações no BD
        status = pieces.lib_mysql.set_bd_ibge(list_files=status['lista'])
                
        # Finaliza o processo e envia email de conclusao.
        if status['code'] == 0:
            pieces.logger.info("Automatização finalizou com sucesso!")
            status_process = True
        else:
            pieces.logger.info("Automatização finalizou com falha!")            
    except Exception as error:
        pieces.logger.error(f" Erro no start_process():{error}")
    
    finally:
        pieces.logger.info(f" [FIM] start_process()")
        return status_process


if __name__ == '__main__':
    for _ in range(3):
        success = start_process()
        if success:
            break
            
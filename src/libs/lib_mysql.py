import pieces
from gvars import *

def set_bd_ibge(list_files=None):
    pieces.logger.info(f'[INICIO] -> set_bd_ibge')

    # Conecta Banco MYSQL
    try:                   
        connection = pieces.mysql.connector.connect(
        host= HOST,  
        port= PORT,
        database= DATABASE,  
        user= USER, 
        password= PASSWORD 
        )

        pieces.logger.info(f"Conectou com sucesso no banco")
        cursor = connection.cursor()

        if connection.is_connected():      
            connected = True
        else:
            connected = False
        
    except pieces.Error as error:
        pieces.logger.error(f"Erro de bando de dados:{error}")
        return {
            "code" : -1 ,
            "message" : error
            }
    
    # Cria a tabela ibge_report
    try:
        if connected:
            query_drop = "DROP TABLE IF EXISTS ibge_report;" 
            query_create ="""
                CREATE TABLE ibge_report (
                CodFile INT NOT NULL AUTO_INCREMENT,
                NomeFile VARCHAR(255),
                PathFile VARCHAR(255),
                DtExtracao DATE,
                PRIMARY KEY (CodFile)
                );
                """
            cursor.execute(query_drop)
            cursor.execute(query_create)
        pieces.logger.info(f"CREATE AND DROP TABLE concluida com sucesso!, table= ibge_report")
    except pieces.Error as error:
        pieces.logger.error(f"Erro ao criar a tabela:{error}") 
        return {
            "code" : -2 ,
            "message" : error
            }           

    try:  
        values = []
        str_output = PATH_OUTPUT.replace("\\","/")
        for idx, file_name in enumerate(list_files, start=1):
            values.append(f"({idx}, '{file_name}', '{str_output}/{file_name}', '{TODAY}')")

        values_str = ", ".join(values)

        # Crie o comando completo de INSERT
        query_insert = f"""
            INSERT INTO ibge_report (CodFile, NomeFile, PathFile, DtExtracao)
            VALUES {values_str};
        """       
    
        cursor.execute(query_insert)
        #Commit para salvar as alterações no banco de dados
        connection.commit()
        pieces.logger.info("Insert realizado com sucesso!")
    except pieces.Error as error:
        pieces.logger.error(f"Erro ao inserir dados:{error}")
        return {
            "code" : -3 ,
            "message" : error
            }
    # Fecha Cursor
    cursor.close()
    # Fecha Banco de Dados
    connection.close()
    return {
            "code" : 0 ,
            "message" : "Sucesso"
            }

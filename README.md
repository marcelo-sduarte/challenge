# Extração de dados do IBGE


# Visão Geral
A Automatização tem por objetivo usar o seleninum para entrar no site "https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html", utiliza o menu localizar
o Censo_Demografico_1991 e baixar todos files. Salva o nome dos files e caminho no bando de dados MySQL.

# Estrutura de Pastas
    - env
    - input
    - output
        - files
        - logs
    - src
        -libs
        

# Instalação
Para usar a Extração de dados do IBGE, siga estes passos:

1.Clone este repositório em sua máquina local:

bash
Copy code
git clone https://github.com/mftechnology/extract_data_ibge.git
Instale as dependências necessárias:

2. Instale as bibliotecas necessárias:
bash
Copy code
pip install -r requirements.txt

3. Configure o repositorio virtual.
bash
Copy code
python -m venv env

4. Revise file [gvars.py] e ajustes os diretorios e credenciais de acesso ao banco que serão utilizados no projeto.
    - Como padrão esta armazenado na constante PATH_PROCESS_FOLDER  = "C:\Users\Documents\Python\Automation" pode ser ajustado conforme diretório de sua preferência.
    - As credenciais do banco podem ser salvos temporarialmente no gvars para teste e em produção pode ser usado o cofre de senhas do windows.        

6. Execute o script principal [src/main.py]:
bash
Copy code
python main.py

7. Todas as bibliotecas usadas no python constam no file [pieces.py]


# Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.

Copyright © 2024 MFTechnology by Marcelo Duarte. Todos os direitos reservados.

#pip install fastapi uvicorn 
#pip install psycopg2
#pip install dotenv

import psycopg2
from dotenv import load_dotenv
import os 

#Carregar .env 
load_dotenv()

def conector():
    try:
        conexao = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexao: {erro}")
        return None, None

conector()


import psycopg2
import pontoescavacao
from datetime import date, datetime

cursor = None
conn = None
def conectar():
    global conn, cursor
    conn = psycopg2.connect(
        dbname="escavacoes",
        user="postgres",
        password="ti@cc",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()
    print("Conectado ao sql")

def fecharconex():
    cursor.close()
    conn.close()
def inserirponto(registro):
    ponto = pontoescavacao.PontoEscavacao(*registro)
    cursor.execute("""
        INSERT INTO pontos_escavacao (tipo_ponto, latitude, longitude, altitude, descricao, data_catalogacao, responsavel)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,(ponto.tipo,ponto.latitude,ponto.longitude,ponto.altitude,ponto.descricao,ponto.data_catalogacao,ponto.responsavel))
    print(ponto.tipo)
    conn.commit()

def listarponto():
    cursor.execute("SELECT * FROM pontos_escavacao")
    conn.commit()
    resultado = cursor.fetchall()
    if(len(resultado)>0):
        for registro in resultado:
            ponto = pontoescavacao.PontoEscavacao(*registro)
            print(ponto)
    else:
        print("tabela vazia")

def apagarpontos():
    cursor.execute("DELETE FROM pontos_escavacao")
    conn.commit()

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
    try:
        ponto = pontoescavacao.PontoEscavacao(*registro)
        cursor.execute("""
            INSERT INTO pontos_escavacao (tipo_ponto, latitude, longitude, altitude, descricao, data_catalogacao, responsavel)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (ponto.tipo, ponto.latitude, ponto.longitude, ponto.altitude, ponto.descricao, ponto.data_catalogacao, ponto.responsavel))

        conn.commit()
        print("Registro inserido com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir ponto: {e}")


def listarponto():
    try:
        cursor.execute("SELECT * FROM pontos_escavacao")  
        resultado = cursor.fetchall()

        if resultado:
            for registro in resultado:
                ponto = pontoescavacao.PontoEscavacao(*registro)
                print(ponto)
        else:
            print("Tabela vazia.")

    except Exception as e:
        print(f"Erro ao listar pontos: {e}")


def apagarpontos():
    try:
        cursor.execute("DELETE FROM pontos_escavacao") 
        registros_apagados = cursor.rowcount 
        conn.commit()  

        if registros_apagados > 0:
            print(f"{registros_apagados} pontos apagados com sucesso!")
        else:
            print("Nenhum ponto foi apagado (a tabela já estava vazia).")

    except Exception as e:
        conn.rollback()  
        print(f"Erro ao apagar pontos: {e}")


def apagarponto(id):
    try:
        cursor.execute("SELECT * FROM pontos_escavacao WHERE id = %s", (id,))
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("DELETE FROM pontosescavacao WHERE id = %s", (id,))
            conn.commit()
            print(f"Ponto de escavação com ID = {id} excluído com sucesso.")
        else:
            print("Não existem pontos de escavação com esse ID")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao apagar ponto com ID = {id}: {e}")

def atualizaponto(id):
    
    
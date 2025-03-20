import psycopg2
import pontoescavacao
import responsavel
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
            INSERT INTO pontos_escavacao (tipo_ponto, latitude, longitude, altitude, descricao, data_catalogacao, id_responsavel)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (ponto.tipo, ponto.latitude, ponto.longitude, ponto.altitude, ponto.descricao, ponto.data_catalogacao, ponto.responsavel))

        conn.commit()
        print("Registro inserido com sucesso!")

    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir ponto: {e}")


def listarponto(orderby=None, filtro=None, reverse=False):
    try:
        if filtro is None:
            filtro = {}  
        sql = "SELECT * FROM pontos_escavacao"
        parametros = ()  
        if filtro:  
            condicoes = [f"{coluna} = %s" for coluna in filtro.keys()]
            sql += " WHERE " + " AND ".join(condicoes)
            parametros = tuple(filtro.values())  
        
        if parametros:
            cursor.execute(sql, parametros)
        else:
            cursor.execute(sql)
        resultado = cursor.fetchall()
        if resultado:
            pontos = [pontoescavacao.PontoEscavacao(*registro) for registro in resultado]
            if(orderby == "id"):
                pontos.sort(key=lambda ponto: ponto.id, reverse=reverse)

                
            for ponto in pontos:
                print()
                print(ponto)
        else:
            print("Nenhum registro encontrado.")

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
            cursor.execute("DELETE FROM pontos_escavacao WHERE id = %s", (id,))
            conn.commit()
            print(f"Ponto de escavação com ID = {id} excluído com sucesso.")
        else:
            print("Não existem pontos de escavação com esse ID")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao apagar ponto com ID = {id}: {e}")

def atualizaponto(atributos):
    try:
        ponto = pontoescavacao.PontoEscavacao(*atributos)
        cursor.execute("SELECT * FROM pontos_escavacao WHERE id = %s", (ponto.id,))
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("""
            UPDATE pontos_escavacao 
            SET tipo_ponto = %s, latitude = %s, longitude = %s, altitude = %s, descricao = %s, data_catalogacao = %s, responsavel = %s
            WHERE id = %s
            """,(ponto.tipo, ponto.latitude, ponto.longitude, ponto.altitude, ponto.descricao, ponto.data_catalogacao, ponto.responsavel, ponto.id))
            conn.commit()
            print("Alterações salvas.")
        else:
            print("Não existem pontos de escavação com esse ID")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao atualizar ponto")

def cadastrar_responsavel(registro):
    try:
        respon = responsavel.Responsavel(*registro)
        cursor.execute("""
            INSERT INTO responsavel (nome, telefone, instituicao, especialidade)
            VALUES (%s, %s, %s, %s)
        """, (respon.nome, respon.telefone, respon.instituicao, respon.especialidade))
        conn.commit()
        print("Cadastro concluído com sucesso")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir ponto: {e}")

def listar_responsavel():
    try:
        cursor.execute("SELECT * FROM responsavel")  
        resultado = cursor.fetchall()

        if resultado:
            for registro in resultado:
                ponto = responsavel.Responsavel(*registro)
                print(ponto)
        else:
            print("Tabela vazia.")

    except Exception as e:
        print(f"Erro ao listar pontos: {e}")

def apagar_responsaveis():
    try:
        cursor.execute("DELETE FROM responsavel")
        registros_apagados = cursor.rowcount
        conn.commit()
        if registros_apagados > 0:
            print(f"{registros_apagados} registros apagados com sucesso.")
        else:
            print("A tabela já estava vazia")
    except Exception as e:
        print(f"Erro ao apagar os registros: {e}")

def atualizar_responsaveis(atributos):
    try:
        respon = responsavel.Responsavel(*atributos)
        cursor.execute("SELECT * FROM responsavel WHERE id = %s ", (respon.id,))
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("""
                UPDATE responsavel
                SET nome = %s, telefone = %s, instituicao = %s, especialidade = %s 
            """, (respon.nome, respon.telefone, respon.instituicao, respon.especialidade))
            conn.commit()
            print("Alterações salvas.")
        else:
            print("Não existe um responsável com esse id.")
    except Exception as e:
        print(f"Erro ao atualizar os responsáveis: {e}")


    
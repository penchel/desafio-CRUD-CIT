import datetime
import conn
from datetime import date, datetime
def leratributos():
    resp = input("Tipo de artefato: ").strip()
    while not resp:
        print("Tipo de artefato vazio ou nulo!")
        resp = input("Tipo de artefato: ").strip()
    tupla = []
    tupla.append(resp)

    resp = float(input("Latitude: "))
    while not resp:
        print("Latitude vazia ou nula!")
        resp = float(input("Latitude: "))
    tupla.append(resp)

    resp = float(input("Longitude: "))
    while not resp:
        print("Longitude vazia ou nula!")
        resp = float(input("Longitude: "))
    tupla.append(resp)

    resp = float(input("Altitude: "))
    tupla.append(resp)

    resp = input("Descrição: ")
    tupla.append(resp)
   
    while True:
        resp = input("Data de Catalogação (DD-MM-YYYY): ").strip()
        try:
            resp = datetime.strptime(resp, "%d-%m-%Y").date()
            break
        except:
            print("Formato inválido")
    tupla.append(resp)
    
    resp = input("Responsável(is): ").strip()
    while not resp:
        print("Tipo de artefato vazio ou nulo!")
        resp = input("Tipo de artefato: ").strip()
    tupla.append(resp)
    return tupla
def excluir():
    id = input("insira o id (insira 'a' para apagar todos os registros): ")
    if id == 'a':
        certeza = input("Tem certeza que quer apagar todos os registros? (S/N): ")
        if certeza == 'S': conn.apagarpontos()
        else: excluir()
    else:
        certeza = input("Tem certeza que quer apagar esse registro? (S/N): ")
        if certeza == 'S': conn.apagarponto(id)
        else: excluir()

def menu():
    conn.conectar()
    #atributos = (1,"Artefato",-1000,100,8000,"Esse artefato foi encontrado perto de uma nação indigena e era usado para",date(2019, 11, 23),"André")
    print("Pontos de Escavação:")
    print("1 - Listar Todos os Pontos")
    print("2 - Inserir Pontos")
    print("3 - Excluir Pontos")
    print("4 - Alterar Informações dos Pontos")
    print("5 - Buscar pontos")
    opcao = input("Escolha sua opção:")
    match opcao:
        case 1:
            conn.listarponto()
        case 2:
            atributos = leratributos()
            atributos.insert(0,1)
            conn.inserirponto(tuple(atributos))
        case 3:
            excluir()
    


    
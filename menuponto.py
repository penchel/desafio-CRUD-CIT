import datetime
import bd
from datetime import date, datetime
def leratributos():
    resp = input("Tipo de artefato: ").strip()
    while not resp:
        print("Tipo de artefato vazio ou nulo!")
        resp = input("Tipo de artefato: ").strip()
    tupla = []
    tupla.append(resp)

    while True:
        resp = input("Latitude: ").strip()
        try:
            resp = float(resp)
            break
        except ValueError:
            print("valor inválido.")
    tupla.append(resp)

    while True:
        resp = input("Longitude: ").strip()
        try:
            resp = float(resp)
            break
        except ValueError:
            print("valor inválido.")
    tupla.append(resp)

    while True:
        resp = input("Altitude: ").strip()
        try:
            resp = float(resp)
            break
        except ValueError:
            print("valor inválido.")
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
        print("Responsável(is) vazio ou nulo!")
        resp = input("Responsável(is): ").strip()
    tupla.append(resp)
    return tupla

def excluir():
    id = input("insira o id (insira 'a' para apagar todos os registros): ")
    if id == 'a':
        certeza = input("Tem certeza que quer apagar todos os registros? (S/N): ")
        if certeza == 'S': bd.apagarpontos()
        else: excluir()
    else:
        certeza = input("Tem certeza que quer apagar esse registro? (S/N): ")
        if certeza == 'S': bd.apagarponto(id)
        else: excluir()

def menu():
    #atributos = (1,"Artefato",-1000,100,8000,"Esse artefato foi encontrado perto de uma nação indigena e era usado para",date(2019, 11, 23),"André")
    print("\nPontos de Escavação:")
    print("1 - Listar Todos os Pontos")
    print("2 - Inserir Pontos")
    print("3 - Excluir Pontos")
    print("4 - Alterar Informações dos Pontos")
    print("5 - Buscar pontos")
    print("0 - Voltar\n")
    opcao = int(input("Escolha sua opção: "))
    match opcao:
        case 1:
            bd.listarponto()
            input("\nEnter - Voltar para o menu")
            menu()
        case 2:
            atributos = leratributos()
            atributos.insert(0,1)
            bd.inserirponto(tuple(atributos))
            input("\nEnter - Voltar para o menu")
            menu()
        case 3:
            excluir()
            input("\nEnter - Voltar para o menu")
            menu()
        case 4:
            id = int(input("Insira o id do ponto de escavação a ser alterado: "))
            atributos = leratributos()
            atributos.insert(0,id)
            bd.atualizaponto(tuple(atributos))
            input("\nEnter - Voltar para o menu")
            menu()
        case 0:
            None

bd.conectar()  
menu()

    
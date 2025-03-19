from datetime import date, datetime
import bd
def leratributos():
    resp = input("Nome: ")
    while not resp.strip():
        print("Nome vazio ou nulo!")
        resp = input("Nome: ").strip()
    tupla = []
    tupla.append(resp)

    resp = input("Telefone (apenas números): ").strip() 
    tupla.append(resp)  

    resp = input("Nome da Insituição: ")
    while not resp.strip():
        print("Nome vazio ou nulo!")
        resp = input("Nome da Insituição: ")
    tupla.append(resp)

    resp = input("Especialidade: ")
    while not resp.strip():
        print("Especialidade vazia ou nula!")
        resp = input("Nome da Insituição: ")
    tupla.append(resp)

    return tupla

bd.conectar()
atributos = leratributos()
atributos.insert(0,1)
bd.cadastrar_responsavel(tuple(atributos))
bd.listar_responsavel()
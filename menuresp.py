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

def excluir():
    id = input("insira o id (insira 'a' para apagar todos os registros): ")
    if id == 'a':
        certeza = input("Tem certeza que quer apagar todos os registros? (S/N): ")
        if certeza == 'S': bd.apagar_responsaveis()
        else: excluir()
    else:
        certeza = input("Tem certeza que quer apagar esse registro? (S/N): ")
        if certeza == 'S': bd.apagar_responsaveis()
        else: excluir()


def menu(): 
    #atributos = (1,"Artefato",-1000,100,8000,"Esse artefato foi encontrado perto de uma nação indigena e era usado para",date(2019, 11, 23),"André")
    print("\nResponsáveis:")
    print("1 - Listar Todos os Responsáveis")
    print("2 - Inserir Responsáveis")
    print("3 - Excluir Responsáveis")
    print("4 - Alterar Informações dos Responsáveis")
    print("5 - Buscar Responsáveis")
    print("0 - Voltar\n")
    opcao = int(input("Escolha sua opção: "))
    match opcao:
        case 1:
            bd.listar_responsavel()
            input("\nEnter - Voltar para o menu")
            menu()
        case 2:
            atributos = leratributos()
            atributos.insert(0,1)
            bd.cadastrar_responsavel(tuple(atributos))
            input("\nEnter - Voltar para o menu")
            menu()
        case 3:
            excluir()
            input("\nEnter - Voltar para o menu")
            menu()
        case 4:
            id = int(input("Insira o id do responsável a ser alterado: "))
            atributos = leratributos()
            atributos.insert(0,id)
            bd.atualizar_responsaveis(tuple(atributos))
            input("\nEnter - Voltar para o menu")
            menu()
        case 0:
            None


import menuponto, menuresp
def menu():
    print("\nBanco de dados CIT")
    print("1 - Pontos de Escavação")
    print("2 - Responáveis")
    print("0 - Sair\n")
    op = input("Escolha sua opção")
    return op

while True:
    op = menu()
    match op:
        case 1:
            menuponto.menu()
        case 2: 
            menuresp.menu()
        case 0:
            break
        case _:
            print("\nInválido\n")

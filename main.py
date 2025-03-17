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

#atributos = (1,"Artefato",-1000,100,8000,"Esse artefato foi encontrado perto de uma nação indigena e era usado para",date(2019, 11, 23),"André")
atributos = leratributos()
atributos.insert(0,1)
conn.conectar()
conn.apagarpontos()
conn.inserirponto(tuple(atributos))
conn.listarponto()
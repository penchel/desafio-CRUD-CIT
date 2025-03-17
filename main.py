import conn
from datetime import date
def leratributos():
    tupla = ()
    print("Tipo de artefato: ")
    resp = input()
atributos = (1,"Artefato",-1000,100,8000,"Esse artefato foi encontrado perto de uma nação indigena e era usado para",date(2019, 11, 23),"André")
conn.conectar()
conn.apagarpontos()
conn.inserirponto(atributos)
conn.listarponto()
from datetime import datetime
class PontoEscavacao:
    def __init__(self,id, tipo, latitude, longitude, altitude, descricao, data_catalogacao, responsavel):
        self.id = id
        self.tipo = tipo
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.descricao = descricao
        self.data_catalogacao = data_catalogacao
        self.responsavel = responsavel
    
    def __str__(self):
        return f"id: {self.id}\ntipo: {self.tipo}\ndata: {self.data_catalogacao.strftime('%d-%m-%Y')}\nresponsavel: {self.responsavel}"
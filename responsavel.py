class Responsavel:
    def __init__(self, id, nome, telefone, instituicao, especialidade):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.instituicao = instituicao
        self.especialidade = especialidade

    def __str__(self):
        return f"id: {self.id}\nnome: {self.nome}\ninstituicao: {self.instituicao}\nespecialidade: {self.especialidade}"
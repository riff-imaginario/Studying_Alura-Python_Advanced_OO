class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.nome    = nome
        self.ano     = ano
        self.duracao = duracao


class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.nome       = nome
        self.ano        = ano
        self.temporadas = temporadas

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)

atlanta = Serie('Atlanta', 2018, 2)

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao}')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')
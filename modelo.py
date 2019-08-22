class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.nome    = nome.title()
        self.ano     = ano
        self.duracao = duracao
        self.like    = 0

    def dar_like(self):
        self.like += 1


class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.nome       = nome.title()
        self.ano        = ano
        self.temporadas = temporadas
        self.like    = 0

    def dar_like(self):
        self.like += 1

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)

atlanta = Serie('Atlanta', 2018, 2)

vingadores.dar_like()
atlanta.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.like}')

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.like}')
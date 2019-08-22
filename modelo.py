class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.__nome    = nome.title()
        self.ano     = ano
        self.duracao = duracao
        self.__like    = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
         return self.__likes

    def dar_like(self):
        self.__like += 1


class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.__nome       = nome.title()
        self.ano        = ano
        self.temporadas = temporadas
        self.__like    = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
         return self.__likes

    def dar_like(self):
        self.__like += 1

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)

atlanta = Serie('Atlanta', 2018, 2)

vingadores.dar_like()
atlanta.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
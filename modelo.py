class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano   = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
         return self.__like

    def dar_like(self):
        self._like += 1


# Filme herda de Programa
class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        self._nome   = nome.title()
        self.ano     = ano
        self.duracao = duracao
        self._like   = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
         return self._like

    def dar_like(self):
        self._like += 1

    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano} - Duracao: {self.duracao} - Likes: {self._like}')


# Serie herda de Programa
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        self._nome      = nome.title()
        self.ano        = ano
        self.temporadas = temporadas
        self._like      = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
         return self.__like

    def dar_like(self):
        self._like += 1

    def imprime(self):
        print(f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._like}')

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
atlanta    = Serie('Atlanta', 2018, 2)

vingadores.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime()
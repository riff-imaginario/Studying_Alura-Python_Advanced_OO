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
        self.__like += 1

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)

atlanta = Serie('Atlanta', 2018, 2)

vingadores.dar_like()
atlanta.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes} - {programa.likes}')
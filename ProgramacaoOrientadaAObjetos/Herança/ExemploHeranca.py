class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

# Herança começa aqui nas classes 'filhas'

class Filme(Programa):   # Definir qual vai ser da classe que vai herdar
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Parte da herança chamar o super().__init__(classe mãe)
        self.duracao = duracao

class Serie(Programa):          # Definir qual vai ser da classe que vai herdar
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)     # Parte da herança chamar o super().__init__(classe mãe)
        self.temporadas = temporadas

# Herança termina aqui

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')
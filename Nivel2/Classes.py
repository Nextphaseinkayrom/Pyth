class User:

    def __init__(self,nome, idade, ano):
        self.nome = nome
        self.idade = idade
        self.ano = ano

user1 = User('FirstUser', 20, 1980)

print(user1.nome)

print(user1.idade)

print(user1.ano)

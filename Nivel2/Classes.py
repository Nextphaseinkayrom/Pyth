class User:
 def __init__(self,nome, idade, ano):
        self.nome = nome
        self.idade = idade
        self.ano = ano

nome = input('Digite seu nome: ')

idade = input('Digite sua idade: ')

ano = input('Digite seu ano:')

infor = User(nome, idade, ano)

print(f"""
    Nome do User: {infor.nome}
    Idade do User: {infor.idade}
    Ano do User: {infor.ano}""")









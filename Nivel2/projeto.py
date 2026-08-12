pessoas = []
class Person:
  def __init__(self, name, vida, idade):
    self.name = name
    self.vida = vida
    self.idade = idade

  def infor(self):
    return f'Nome: {self.name} | Vida: {self.vida} | Idade: {self.idade}'


while True:
 print("""
 1 - Ver cadastros
 2 - Fazer cadastros
 3 - Sair""")
 pergunta = int(input('digite oque você deseja'))

 if pergunta == 1:
    print(f'Os cadastrados no momento são. . .\n')
    for pessoas in pessoas:
        print(pessoas.infor())



 elif pergunta == 2:
    print('Indo ao registro')
    perg_1 = str(input('Name: '))
    perg_2 = int(input('Vida: '))
    perg_3 = int(input('Idade: '))

    pessoa = Person(perg_1, perg_2, perg_3)
    pessoas.append(pessoa)

    for pessoa in pessoas:
     print(pessoa.infor())
 else:
    print('Saindo')
    break



















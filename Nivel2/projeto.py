pessoas = []
class Person:
  def __init__(self, nome, vida, idade):
    self.nome = nome
    self.vida = vida
    self.idade = idade
  def infor(self):
    return (f'Nome: {self.nome} | Vida: {self.vida} | Idade: {self.idade}')
for i in range(3):

  perg_1 = str(input('Nome: '))
  perg_2 = int(input('Vida: '))
  perg_3 = int(input('Idade: '))
  p_1 = Person(perg_1, perg_2, perg_3)
  pessoas.append(p_1)

for pessoa in pessoas:
 print(pessoa.infor())


















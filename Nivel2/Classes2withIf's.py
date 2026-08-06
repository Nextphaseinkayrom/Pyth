class Ifs:
  def __init__(self,nome, idade):
     self.nome = nome
     self.idade = idade

def verificacao():
 nome = str(input('digite seu nome: '))
 idade = int(input('digite sua idade: '))
 infor = Ifs(nome, idade)

 if nome == 'kayrom' and idade == 18:
    print(f'Identificação permitida 2/2\nAs informações são {infor.nome} E a idade {infor.idade}')

 else:
    print('. . . Identificação negada, se retire. . .')





verificacao()
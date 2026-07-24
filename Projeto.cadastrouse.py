pessoas = []
def area1():
  print('\nSeja bem vindo a área de cadastro\nPor favor digite seu nome abaixo. . .')
  pessoas.append({
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "altura": float(input("Altura: "))
    })
  print(f'Cadastro feito com Sucesso. . .')


def area0():
 while True:
  print("""
       Olá, seja bem vindo User(??)
       Usamos formas de cadastrar seu úsuario
       Basta escolher qual menu deseja no momento\n
       1 - - Fazer Cadastro\n
       2 - - Listar Cadstro's\n
       3 - - Buscar Cadastro's\n
       4 - - Sair do Programa
    """)
  pergunta = int(input("Digite oque você deseja"))

  if pergunta == 1:
      print("indo . . .")
      area1()

  elif pergunta == 2:
      print(f'Usuarios cadastrados no momento são\n{pessoas}')

  elif pergunta == 3:
      print('. . . .')
  elif pergunta == 4:
      print("Saindo do programa. . .")
      break

  else:
      print('Saindo. . .')
      area0()

area0()
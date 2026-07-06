# Esse projeto foi criado com Funções
# Na intenção onde o usuario pode ser transferido de Menu 1 E Menu 2
# E caso ele quiser sair, Ele apenas aperte qualquer tecla não especificadas no Print do menu 1 e 2
# Esse projeto foi por pura prática
def menu_1():
  print('menu 1')
  print('1 -- Ir pro 2')
  print('Botão-alt = Sair')

  opcao = input('Digite oque quer')

  if opcao == '1':
   return menu_2()

  else:
    print('Saindo. . .')


def menu_2():
  print('Menu 2')
  print('1 -- Voltar pro 1')
  print('B-alt = sair')

  opcaodois = input('Digite oque quer')

  if opcaodois == '1':
    return menu_1()

  else:
    print('Saindo. . .')

menu_1()
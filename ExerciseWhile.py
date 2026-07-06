# Foi mais um exercicio padrão para ver os if e enquanto não for 3. Ele fica repetindo.
menu = 1
print('1 --- Entrar')
print('2 --- Configurações')
print('3 --- Sair')

while menu != 3:
    menu = int(input('Oque você deseja?'))


    if menu == 1:
        print('Entrando. . .')
        print('Bem vindo')

    elif menu == 2:
        print('Indo as configurações . . .')

    elif menu == 3:
        print('Saindo. . .')

    else:
        print('Invalido . . .')
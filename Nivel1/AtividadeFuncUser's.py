infuser0 = {
    'Nome': 'João',
    'idade': '19',
    'Altura': '1.84'
}
infuser1 = {
    'Nome': 'Maria',
    'idade': '19',
    'Altura': '1.65'
}
#Função user0
def func_user0():
   print("Bem vindo User0")
   print('1 - Sair')

   senha0 = int(input("Qual a senha do User0?"))

   if senha0 == 1342:
       print(f'Bem vindo User0\nSuas Informações\n{infuser0}')

   elif senha0 == 1:
        print('Voltando')
        func_de_users()
   else:
       print('Saia.')
#Fim do User0

#Função Do user 1
def func_user1():
    print("Bem vindo User1")
    print('1 - Sair')
    senha1 = int(input("Qual a senha do User0?"))

    if senha1 == 1322:
        print(f'Bem vindo User0\nSuas Informações\n{infuser0}')


    elif senha1 == 1:
        print('Ok voltando')
        func_de_users()

    else:
        print('Saia.')
#Fim do user1


def func_de_users ():
    print("""--- Função D User's --- 
0 - User0
1 - User1
Escolha qual User deseja entrar""")

    pergunta = int(input('Qual User deseja: '))

    if pergunta == 0:
        print('User0?')
        func_user0()

    if pergunta == 1:
        print('User1?')
        func_user1()


func_de_users()


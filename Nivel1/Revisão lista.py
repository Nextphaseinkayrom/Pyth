# Aqui foi um revisão/exercicio Para anotar na mente sobre Lista

nomes = ['joana', 'joão']
bloqueados = ['marcos']

def apresentar():
    print('Bem vindo desconhecido apenas 3. . .\npessoas conseguem entrar aqui. . .\nMais obviamente Uma dessas 3 pessoa não podem entrar aqui. . .')

    pergunta = input('Digite seu nome: ')



    if pergunta in nomes:
     print(f'Bem vindo {pergunta}')
    elif pergunta in nomes:
     print(f'Bem vindo {pergunta}')
    elif pergunta in bloqueados:
     print(f'Você não pode entrar me desculpe {pergunta}')
    else:
     print('Tá errado, saia')

apresentar()
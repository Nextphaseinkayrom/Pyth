# Projeto que faz contas, onde as 3 opções abaixo entrega um valor diferente
def menu():
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Dividir')
    print('4 - Sair do Programa')

    cmc = int(input('Digite um número do programa: '))
    return cmc


def soma():
    print('Soma dos números')
    numeroum = int(input('Digite um número: '))
    numerodois = int(input('Digite outro número: '))
    resultado = numeroum + numerodois
    print(f'O resultado é {resultado}')


def multi():
    print('Multiplicar')
    numeroum = int(input('Digite um número: '))
    numerodois = int(input('Digite outro número: '))
    resultado = numeroum * numerodois
    print(f'O resultado é {resultado}')


def div():
    print('Dividindo número')
    numeroum = int(input('Digite um número: '))
    numerodois = int(input('Digite outro número: '))

    if numerodois == 0:
        print('Não é possível dividir por zero.')
    else:
        resultado = numeroum / numerodois
        print(f'O resultado é {resultado}')


cmc = menu()

if cmc == 1:
    soma()

elif cmc == 2:
    multi()

elif cmc == 3:
    div()

elif cmc == 4:
    print('Saindo do programa...')

else:
    print('Opção inválida')
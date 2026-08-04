from pickletools import int4

moveis = ['casa', 'lar', 'hotel']

print('Olá temos um bom serviço pra você onde voc~e g anha um certo valor se você digitar outro')

print('1 -- Repita o numero 1 em 20')
print('2 -- Repita o numero 2 em 30')
print('3 -- ???')

per = int(input('Oque deseja?'))




if per == 1:
 for numero in range(30):
    print(f'Pronto você repetiu o 1 em {numero} vezes')

elif per == 2:
    for numero in range(1,10):
        print(f'Pronto repetiu o 1 em {numero} vezes')
elif per == 4:
    moveis.pop('eiai')

elif per == 3:
    print(f'No momentos não temos essas palavras\ndisponiveis de moveis que você pode chamar de casa {moveis}')

else:
        print('Não está disponivel')
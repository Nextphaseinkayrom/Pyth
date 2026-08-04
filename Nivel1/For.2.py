pessoas = []
for i in range(3):
    nome = str(input('D. U.Nome: '))
    idade = int(input('D. u.Idade: '))

    armazenador = [nome, idade]
    pessoas.append(armazenador)

print('Personagem sendo criado 1 segundo. . .')
print('Criação completa!!')


for armazenador in pessoas:
 print(f'Nome| {armazenador[0]}\n Idade | {armazenador[1]}\n')
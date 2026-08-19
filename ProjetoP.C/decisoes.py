from produtos import Loja
from produtos import produto1, produto2, pergunta_1
from menu_inicial import carrinho, perg_0, total, carrinho
from confirmacao import pessoas, pessoa1, pessoa2, conf_compra



if perg_0 == 1:
    nome = input("Digite seu nome")
    pix = int(input("Digite sua senha "))

    if nome == pessoa1["Nome"]:
        pessoa = pessoa1
        print('Entrando na área de senha. . .')

    if pix == pessoas["Senha"] and total <= ["Saldo"]:
        print(f'Primeira etapa feita {total}$ Valor da compra')

    if pergunta_1 == 1:
    if produto1.estoque >= 1:
        carrinho.append(produto1)
        produto1.estoque -= 1
        print("Produto adicionado!")
    else:
        print("Sem estoque")

elif pergunta_1 == 2:
    if produto2.estoque >= 1:
          carrinho.append(produto2)
          produto2.estoque -= 1
          print('Produto adicionado!')
    else:
          print('Sem estoque')

elif pergunta_1 == 3:
    if carrinho:
          print('Os produtos no momentos\n')
    else:
        print('Sem nada no carrinho até agora. . .')
    for produto in carrinho:
         print(f'Produto/s : {produto.nome} ')
         print(f'Valor/es : {produto.valor}\n')

elif pergunta_1 == 4:
    if carrinho:
       print("Indo à confirmação de compra")
    for produto in carrinho:
     total += produto.valor
     conf_compra()
     break
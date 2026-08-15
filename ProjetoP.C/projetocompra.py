# Primeiro estágio > --- compra

class Loja:
 def __init__(self, nome, valor, estoque):
    self.nome = nome
    self.valor = valor
    self.estoque = estoque

produto1 = Loja("Roupa de luxo para festas", 200, 1)
produto2 = Loja("Roupa de estampa de fogo", 100, 2)
produto3 = Loja("Calça social", 250, 4)
produto4 = Loja("Short para as férias", 20, 5)
carrinho = []
while True:

  print(f"""Olá seja bem vindo a loja de Roupas
  Itens disponiveis no momento são. . .
   1 - Roupa de luxo para Festas | Estoque disponiveis >-{produto1.estoque}
   2 - Roupa de estampa de fogo | Estoques disponiveis >- {produto2.estoque} 
   3 - Calça Social | Estoques disponiveis >- {produto3.estoque}
   4 - Short para as férias | Estoques disponiveis >- {produto4.estoque}
   5 - Ver carrinho
   6 - Ir confirmar compra
   7 - Desejo sair ou só estou dando uma volta :(. . .""")

  pergunta_1 = int(input('Oque deseja?'))


  #Área de decisões

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
      if produto3.estoque >= 1:
          carrinho.append(produto3)
          produto3.estoque -= 1
          print('Produto adicionado! ')
      else:
          print('Sem estoque')
  elif pergunta_1 == 4:
      if produto4.estoque >= 1:
          carrinho.append(produto4)
          produto4.estoque -= 1
      else:
          print('Sem estoque')

  elif pergunta_1 == 5:
      if carrinho:
          print('Os produtos no momentos')
      else:
        print('Sem nada no carrinho até agora. . .')
      for produto in carrinho:
         print(f'Produto/s : {produto.nome} ')
         print(f'Valor/es : {produto.valor}\n')

  elif pergunta_1 == 6:
      print("Indo a confirmação de compra")
      import confirm


#80% Do trabalho foi feito, oque é necessário é
#Fazer a área de confirmação de compra
#Transferir os resultados do carrinho
#Confirmar a compra
#E pergunta se deseja voltar ou sair do programa
#Caso queira, transferir o usuario para este programa novamente
#Caso não, finalizar de lá mesmo







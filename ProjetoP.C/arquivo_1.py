def conf_compra():
    print(f""""
    Bem vindo a área de pagamento
    
    1 - Pix
    2 - Voltar
    3 - Finalizar programa
    -- OBS a compra deu {total}""")

    perg_0 = int(input('Digite oque vocẽ deseja'))

    from arquivo_2 import pessoas

    if perg_0 == 1:
       nome = input("Digite seu nome")
       pix = int(input("Digite sua senha "))

       if nome == pessoa1["Nome"]:
           pessoa = pessoa1
           print('Entrando na área de senha. . .')

       if pix == pessoas["Senha"] and total <= ["Saldo"]:
          print(f'Primeira etapa feita {total}$ Valor da compra')
# Erros achados no programa é que ele não puxa informações do outro arquivo de pagamento
# Então irá ficar pendente o projeto até eu aprender algo que possa aprimorar

class Loja:
 def __init__(self, nome, valor, estoque):
    self.nome = nome
    self.valor = valor
    self.estoque = estoque

produto1 = Loja("Roupa de luxo para festas", 150, 1)
produto2 = Loja("Roupa de estampa de fogo", 50, 2)
carrinho = []
total = 0

while True:
  print(f"""Olá seja bem vindo a loja de Roupas
  Itens disponiveis no momento são. . .
   1 - Roupa de luxo para Festas | Ets dispo >-{produto1.estoque} Valor >- {produto1.valor}$
   2 - Roupa de estampa de fogo | Ets disponiveis >- {produto2.estoque} Valor >- { produto2.valor}$ 
   3 - Ver carrinho
   4 - Ir confirmar compra
   5 - Desejo sair ou só estou dando uma volta :(. . .""")
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

class Loja:
 def __init__(self, nome, valor, estoque):
    self.nome = nome
    self.valor = valor
    self.estoque = estoque

produto1 = Loja("Roupa de luxo para festas", 150, 1)
produto2 = Loja("Roupa de estampa de fogo", 50, 2)

while True:
  print(f"""Olá seja bem vindo a loja de Roupas
  Itens disponiveis no momento são. . .
   1 - Roupa de luxo para Festas | Ets dispo >-{produto1.estoque} Valor >- {produto1.valor}$
   2 - Roupa de estampa de fogo | Ets disponiveis >- {produto2.estoque} Valor >- { produto2.valor}$ 
   3 - Voltar para Menu inicial""")
  pergunta_1 = int(input('Oque deseja?'))
class Cachorros:
 def __init__(self, nome, idade, vida):
  self.nome = nome
  self.idade = idade
  self.vida = vida

rex = Cachorros('rex', 5, 100)

print(f"Nome: {rex.nome}")
print(f"Idade: {rex.idade}")
print(f"Vida: {rex.vida}")

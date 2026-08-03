# Criando uma classe chamada Cachorros
class Cachorros:

    # Método construtor, executado quando criamos um objeto
    def __init__(self, nome, idade, vida):

        # Guarda o nome recebido dentro do objeto
        self.nome = nome

        # Guarda a idade do cachorro
        self.idade = idade

        # Guarda a quantidade de vida do cachorro
        self.vida = vida


# Criando um objeto (instância) da classe Cachorros
rex = Cachorros('rex', 5, 100)

# Exibindo o atributo nome do objeto rex
print(f"Nome: {rex.nome}")

# Exibindo o atributo idade do objeto rex
print(f"Idade: {rex.idade}")

# Exibindo o atributo vida do objeto rex
print(f"Vida: {rex.vida}")

#Classes criadas pelo chatgpt
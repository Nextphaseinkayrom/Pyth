# Área da função
# Essa função recebe um nome e devolve esse mesmo nome.
def pegar_nome(nome):
    return nome


# Aqui o input pede o nome para o usuário.
# O nome digitado fica guardado na variável pergunta_1.
pergunta_1 = input("Digite seu nome: ")

# Aqui eu envio pergunta_1 para a função pegar_nome.
# O return da função devolve o nome e guarda em resultado.
resultado = pegar_nome(pergunta_1)


# Área dos ifs
# Aqui o código verifica qual nome foi digitado.
if resultado == "user1":
    print("Não pode entrar!")

elif resultado == "user2":
    print(f"Bem vindo {resultado}!")

else:
    print("Fora!")


# input pega o valor
# função recebe o valor
# return devolve o valor
# variável guarda o retorno
# if usa o valor para decidir
#Comentários feito pelo Codex.
#Porque minha linguagem é informal e só entendivel a mim mesmo.

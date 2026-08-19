def pessoas(**kwargs):
    return kwargs
pessoa1={
            "Nome": "João",
            "Saldo": 340,
            "Senha": 1032
},
pessoa2={
            "Nome": "Dayane",
            "Saldo": 200,
            "Senha": 9203
        }

from menu_inicial import total

def conf_compra():
    print(f""""
    Bem vindo a área de pagamento

    1 - Pix
    2 - Voltar
    3 - Finalizar programa
    -- OBS a compra deu {total}""")


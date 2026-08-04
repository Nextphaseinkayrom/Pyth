from unittest import case


#Um exercicio aonde eu tentei aprender Match e Usar emojis no python

print('Yo.😁 Escolha um dia da semana que você gosta 1-7')

pergunta = int(input('Digite Um numero. . .'))

match pergunta:
    case 1:
       print('Segunda😢')
    case 2:
        print('terceira 😊')
    case 3:
        print('Quarta😒')
    case 4:
        print('Quinta👍👍')
    case 5:
        print('Sexta😘')
    case 6:
        print('Sabado? Boa😂')
    case 7:
        print('Domingo A noite😒')

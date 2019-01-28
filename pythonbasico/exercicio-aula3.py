idade = input('Digite sua idade: ')
peso = input('Digite sua peso: ')
altura = input('Digite sua altura: ')

if int(idade) > 18 and float(peso) >= 60 and float(altura) >= 1.70:
    print('Apto a entrar no Exército')
else:
    print('Não apto a entrar no exército')

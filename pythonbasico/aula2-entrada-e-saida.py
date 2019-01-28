nome = 'Maiki' # exemplo de comentario
idade = 38
altura = 1.73

tipo_nome = type(nome)
print(nome, tipo_nome)

print(nome, 'tem', idade, 'anos e', altura, 'de altura')
print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')

frase = nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura'
print(frase)

dig_nome = input('Digite seu nome: ')
dig_idade = input('Digite sua idade: ')
dig_altura = input('Digite sua altura: ')

print(dig_nome, 'tem', dig_idade, 'anos e', dig_altura, 'de altura')

'''
EXERCICIO: Faça um formulário que pergunte:
nome, cpf, endereço, idade, altura e telefone
e imprima isso em um relatório organizado
'''

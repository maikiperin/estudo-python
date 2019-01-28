quantidade_pessoas = int(input('Digite a quantidade de pessoas a serem convidadas para a festa: '))
pessoas = []
nome_pessoa = ''
i = 0

while i < quantidade_pessoas:
    nome_pessoa = input('Digite o nome do ' + str(i + 1) + 'º convidado: ')
    pessoas.append(nome_pessoa)
    i += 1

print(pessoas)
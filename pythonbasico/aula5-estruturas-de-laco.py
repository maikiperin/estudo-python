nomes = ['João', 'Maria', 'Joaquim']

for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])

lista_numeros = range(0, 100, 2)
for item in lista_numeros:
    print(item)

palavra = 'Maiki Perin'

for letra in palavra:
    print(letra)

i = 0

while i < 10:
    print('i menor que 10:', i)
    i = i + 1

print('Acabou o while, i igual a:', i)

lista_frutas = ['maca', 'abacaxi', 'pera', 'uva', 'goiaba']

contador = 0

for fruta in lista_frutas:
    contador += 1

print(contador)
print(len(lista_frutas))

numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

'''
EXERCICIO: faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
Após isso imprimir todos os nomes da lista
'''
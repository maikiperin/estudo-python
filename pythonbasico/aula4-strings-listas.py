frase = 'Oi, tudo bem?'
lista_nomes = ['João', 'Maria', 'Joaquim']

print(frase[0:2])
print(frase[0:13:1])
print(frase[0:13:2])
print(frase[: : -1])
print(frase.lower())

frase_separada = frase.split(',')
print(frase_separada)
print(frase_separada[1])

frase_nova = frase + ' Tudo jóia!'
print(frase_nova)

print(type(lista_nomes))
print(lista_nomes)
print(lista_nomes[0:2])
print(lista_nomes[-1])

lista_nomes.append('Joana')
print(lista_nomes)

lista_nomes.remove('João')
print(lista_nomes)

lista_nomes.insert(0, 'João')
print(lista_nomes)

lista_nomes[3] = 'Lucas'
print(lista_nomes)

print(lista_nomes.count('João'))

print(len(lista_nomes))
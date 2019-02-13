#1
'''
vetor = [1, 2, 3, 4, 5]

for numero in vetor:
    print(numero)
'''

#2
'''
vetor = [10.0, 11.34, 9.98, 3.23, 6]

vetor.reverse()

print(vetor)
'''

#3
'''
cont = 0
notas = []

while cont < 4:
    cont += 1
    nota = float(input('Informe a nota ' + str(cont) + ': '))
    notas.append(nota)

print('A notas informadas foram', notas)
print('A media das notas e', sum(notas) / len(notas))
'''
#4
'''
vetor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

consoantes = []

for letra in vetor:
    if letra not in ('a', 'e', 'i', 'o', 'u'):
        consoantes.append(letra)

print('Foram informadas ' + str(len(consoantes)) + ' consoantes: ' + str(consoantes))
'''

#5
'''
cont = 0
vetor = []
vetor_par = []
vetor_impar = []
resto = 0

while cont < 20:
    cont += 1
    numero = int(input('Digite o numero ' + str(cont) + ': '))
    vetor.append(numero)
    resto = numero % 2

    if resto == 0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print(vetor)
print(vetor_par)
print(vetor_impar)
'''
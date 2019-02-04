#1
'''
while True:
    nota = float(input('Informe uma nota (entre 0 e 10): '))
    if nota < 0 or nota > 10:
        print('Numero digitado invalido, favor informar nota (entre 0 e 10)')
    else:
        break
'''

#2
'''
while True:
    usuario = input('Informe um usuario: ')
    senha = input('Informe sua senha: ')
 
    if senha == usuario:
        print('A senha nao pode ser igual ao usuario, favor informar novos dados')
    else:
        break
'''

#3
'''
while True:
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    salario = float(input('Informe seu salario: '))
    sexo = input('Informe seu sexo: ')
    est_civil = input('Informe seu estado civil: ')

    if len(nome) < 3:
        print('O nome deve conter três ou mais caracteres')
    elif idade < 0 or idade > 150:
        print('A idade nao pode ser inferior a 0 ou maior que 150')
    elif salario <= 0:
        print('Salario deve ser maior que 0 (zero)')
    elif sexo != 'f' and sexo != 'm':
        print('Sexo deve ser igual a "f" ou "m"')
    elif est_civil not in ('s', 'c', 'v', 'd'):
        print('Os estados civis validos sao: "s" (solteiro) ou "c" (casado) ou "v" (viuvo) ou "d" (divorciado)')
    else:
        break
'''

#4
'''
pais_a = 80000
pais_b = 200000

cresc_a = 3 / 100
cresc_b = 1.5 / 100

ano = 0

while True:
    pais_a += int((pais_a * cresc_a))
    ano += 1
    if pais_a <= pais_b:
        print(str(ano) + ' ano(s) depois, populacao pais A: ' + str(pais_a) + ' populacao pais B: ' + str(pais_b))
    else:
        break
'''

#5
#idem 4

#6
'''
numero = 0
impressao = ''

while numero < 20:
    numero += 1
    #print(numero)

    impressao += str(numero) + '\t'

print(impressao)
'''

#7
'''
numero = 1
maior = 0
aux = 0

while numero <= 5:
    aux = float(input('Digite o ' + str(numero) + ' numero: '))
    if numero == 1:
        maior = aux
    else:
        if aux > maior:
            maior = aux
    numero += 1

print('O maior numero e', maior)
'''

#8
#idem7

#9
'''
numero = 1

while numero <= 50:
    if numero % 2 != 0:
        print(numero)
    numero += 1
'''

#10
'''
numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))

if numero1 > numero2:
    while numero2 <= numero1:
        print(numero2)
        numero2 += 1
elif numero1 < numero2:
    while numero1 <= numero2:
        print(numero1)
        numero1 += 1
else:
    print('Os numeros nao podem ser iguais')
'''

#11
#idem 10

#12
'''
numero = int(input('Qual numero deseja ver a tabuada: '))
x = 1

print('Tabuada de ' + str(numero) + ':')

while x <= 10:
    print(str(numero) + ' X ' + str(x) + ' = ' + str(numero * x))
    x += 1
'''

#13
'''
base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
aux = 1
resultado = 1

while aux <= expoente:
    resultado *= base
    aux += 1

print('Resultado', resultado)
'''

#14
'''
aux = 1
resto = 0
conjunto_par = set()
conjunto_impar = set()

while aux <= 10:
    numero = int(input('Informe um numero: '))
    resto = numero % 2

    if resto == 0:
        conjunto_par.add(numero)
    else:
        conjunto_impar.add(numero)
    aux += 1

print('Numeros pares', conjunto_par)
print('Numeros impares', conjunto_impar)
'''

#15
'''
a = 1
b = 1
lista = []

lista.append(1)

while b < 100:
    c = a
    a = b
    b = a + c
    lista.append(a)

print(lista)
'''

#16
#idem 15

#17
'''
numero = int(input('Informe o numero que deseja calcular seu fatorial: '))
fat = 1
i = 2

while i <= numero:
    fat *= i
    i += 1

print('O fatorial de ' + str(numero) + ' e', fat)
'''

#18
'''
aux = True
soma = 0
numero = []

while aux:
    num = int(input('Digite o numero ou 0 para finalizar o programa: '))
    if num != 0:
        numero.append(num)
    else:
        break

print('Soma', sum(numero))
print('Menor Valor', min(numero))
print('Maior Valor', max(numero))
'''

#19
'''
aux = True
soma = 0
numero = []

while aux:
    num = int(input('Digite o numero ou -1 para finalizar o programa: '))
    if num != -1:
        if num >= 0 and num <= 1000:
            numero.append(num)
        else:
            print('Numero invalido, fora da faixa entre 0 e 1000')
    else:
        break

print('Soma', sum(numero))
print('Menor Valor', min(numero))
print('Maior Valor', max(numero))
'''

#20
'''
aux = True

while aux:
    numero = int(input('Informe o numero que deseja calcular seu fatorial: '))
    if numero > 0 and numero < 16:
        fat = 1
        i = 2

        while i <= numero:
            fat *= i
            i += 1
        print('O fatorial de ' + str(numero) + ' e', fat)
    else:
        print('Permitido calcular o fatorial de números inteiros positivos e menores que 16')
'''

#21
'''
numero = int(input('Informe o numero: '))
divisores = 0

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        divisores += 1

if divisores == 2:
    print('Numero primo')
else:
    print('Nao e numero primo')
'''

#22
'''
numero = int(input('Informe o numero: '))
divisores = 0
lista_divisores = []

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        divisores += 1
        lista_divisores.append(divisor)

if divisores == 2:
    print('Numero primo')
else:
    print('Nao e numero primo')
    print('Seus divisores', lista_divisores)
'''

#23
#idem 22

#24
'''
contador = 0
soma = 0
media = 0

while True:
    numero = int(input('Informe um numero ou 0 para calcular a media: '))
    if numero == 0:
        break
    else:
        soma += numero
        contador += 1

media = soma / contador
print('A media entre os numeros digitados e', media)
'''

#25
contador = 0
soma = 0
media = 0

while True:
    idade = int(input('Informe sua idade ou 0 para calcular a media da turma: '))
    if idade == 0:
        break
    else:
        soma += idade
        contador += 1

media = soma / contador
if media >= 0 and media <= 25:
    print('A turma e jovem')
elif media >= 26 and media <= 60:
    print('A turma e adulta')
else:
    print('A turma e idosa')


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
'''
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
'''

#26
'''
contador = 0
cand1 = 0
cand2 = 0
cand3 = 0

eleitores = int(input('Informe o numero de eleitores: '))

while contador < eleitores:
    contador += 1
    voto = int(input('Favor votar no candidato 1 ou 2 ou 3: '))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    else:
        cand3 += 1

print('O numero de votos para o candidato 1 e', cand1)
print('O numero de votos para o candidato 2 e', cand2)
print('O numero de votos para o candidato 3 e', cand3)
'''

#27
'''
contador = 0
soma = 0

turmas = int(input('Informe o numero de turmars: '))

while contador < turmas:
    contador += 1
    alunos = int(input('Informe quantidade de alunos para a turma ' + str(contador) + ' : '))
    soma += alunos

print('A media de alunos por turma e', soma / turmas)
'''

#28
'''
contador = 0
soma = 0

cds = int(input('Informe a quantidade de CDs: '))

while contador < cds:
    contador += 1
    valor = float(input('Informe o valor pago no CD ' + str(contador) + ' : '))
    soma += valor

print('O valor investido e', soma)
print('O valor medio por CD e', soma / cds)
'''

#29
'''
contador = 0
preco = 1.99

while contador < 50:
    contador += 1
    print(str(contador) + ' - R$ {:.2f}'.format(contador * preco))
'''

#30
'''
contador = 0
preco = float(input('Informe o valor do pao : '))

while contador < 50:
    contador += 1
    print(str(contador) + ' - R$ {:.2f}'.format(contador * preco))
'''

#31
'''
total = 0
contador = 0
lista = []

while True:
    contador += 1
    valor = float(input('Informe o valor do produto ' + str(contador) + ': '))
    total += valor
    if valor == 0:
        break
    else:
        lista.append('Produto ' + str(contador) + ': R$ {:.2f}'.format(valor))

print('Lojas Tabajara')
for produto in lista:
    print(produto)
print('Total: R$ {:.2f}'.format(total))
dinheiro = float(input('Informe o valor em dinheiro: '))
troco = dinheiro - total
print('Dinheiro: R$ {:.2f}'.format(dinheiro))
print('Troco: R${:.2f}'.format(troco))
'''

#32
'''
fat = 1
i = 2
lista = []
calculo = ''
tamanho = 0
contador = 0

numero = int(input('Informe o numero que deseja calcular seu fatorial: '))

lista.append(fat)

while i <= numero:
    lista.append(i)
    fat *= i
    i += 1

tamanho = len(lista)
lista.sort(reverse=True)

for aux in lista:
    contador += 1
    if contador != tamanho:
        calculo += str(aux) + ' . '
    else:
        calculo += str(aux)

print('O fatorial de: ' + str(numero))
print(str(numero) + '! = ' + calculo + ' = ' + str(fat))
'''

#33
'''
aux = True
lista = []

while aux:
    temperatura = int(input('Digite uma temperatura ou 0 para finalizar o programa: '))
    if temperatura != 0:
        lista.append(temperatura)
    else:
        break

print('Media', sum(lista) / len(lista))
print('Menor Valor', min(lista))
print('Maior Valor', max(lista))
'''

#34
#idem 21

#35
'''
numero = int(input('Informe o numero: '))
divisores = 0
contador = 1
lista = []

while contador <= numero:
    for divisor in range(1, contador + 1):
        if contador % divisor == 0:
            divisores += 1

    if divisores == 2:
        lista.append(contador)
    divisores = 0
    contador += 1

print(lista)
'''
#36
'''
lista = []
contador = 0

tabuada = int(input('Informe o numero para montagem da tabuada: '))
inicio = int(input('Informe inicio do calculo: '))
fim = int(input('Informe fim do calculo: '))

contador = inicio

if fim < inicio:
    print('O fim do calculo nao pode ser inferior ao inicio do calculo')
else:
    while contador <= fim:
        lista.append(str(tabuada) + ' X ' + str(contador) + ' = ' + str(tabuada * contador))
        contador += 1

print('Montar a tabuada de:', tabuada)
print('Comecar por:', inicio)
print('Terminar em:', fim)
print()
print('Vou montar a tabuada de ' + str(tabuada) + ' começando em ' + str(inicio) + ' e terminando em ' + str(fim) + ' :')

for aux in lista:
    print(aux)
'''

#37
'''
lista_cliente = []
lista_altura = []
lista_peso = []

maior_altura = 0
pos_maior_altura = 0
menor_altura = 0
pos_menor_altura = 0
maior_peso = 0
pos_maior_peso = 0
menor_peso = 0
pos_menor_peso = 0

while True:
    codigo = input('Informe o seu codigo ou 0(zero) para encerrar o programa: ')
    if codigo == '0':
        break
    else:
        altura = float(input('Informe o sua altura: '))
        peso = float(input('Informe o seu peso: '))
        lista_cliente.append(codigo)
        lista_altura.append(altura)
        lista_peso.append(peso)

maior_altura = max(lista_altura)
pos_maior_altura = lista_altura.index(maior_altura)
print('Cliente com maior altura e ' + str(lista_cliente[pos_maior_altura]) + ' com a altura de ' + str(maior_altura))

menor_altura = min(lista_altura)
pos_menor_altura = lista_altura.index(menor_altura)
print('Cliente com menor altura e ' + str(lista_cliente[pos_menor_altura]) + ' com a altura de ' + str(menor_altura))

maior_peso = max(lista_peso)
pos_maior_peso = lista_peso.index(maior_peso)
print('Cliente com maior peso e ' + str(lista_cliente[pos_maior_peso]) + ' com o peso de ' + str(maior_peso))

menor_peso = min(lista_peso)
pos_menor_peso = lista_peso.index(menor_peso)
print('Cliente com menor peso e ' + str(lista_cliente[pos_menor_peso]) + ' com o peso de ' + str(menor_peso))

print('A media das alturas dos clientes e', round(sum(lista_altura) / len(lista_altura), 2))
print('A media dos pesos dos clientes e', round(sum(lista_peso) / len(lista_peso), 2))
'''

#38
'''
from datetime import datetime

percentual_aumento = 1.5
salario = 1000
novo_salario = 1000 + (1000 * (percentual_aumento / 100))
ano = 1997

now = datetime.now()
ano_atual = now.year

while ano <= ano_atual:
    percentual_aumento *= 2
    novo_salario = novo_salario + (novo_salario * (percentual_aumento / 100))
    print('Salario em ' + str(ano) + ' e ' + str(round(novo_salario, 2)) + ' aplicado reajuste de ' + str(percentual_aumento) + '%')
    ano += 1

print()
print('Salario atual e', round(novo_salario, 2))
'''

#39
'''
aux = 0
lista_codigo = []
lista_altura = []


while aux < 10:
    codigo = input('Informe o codigo do aluno: ')
    altura = float(input('Informe a altura do aluno:'))

    lista_codigo.append(codigo)
    lista_altura.append(altura)

    aux += 1

maior_altura = max(lista_altura)
pos_maior_altura = lista_altura.index(maior_altura)

menor_altura = min(lista_altura)
pos_menor_altura = lista_altura.index(menor_altura)

print('O aluno mais alto e: codigo ' + lista_codigo[pos_maior_altura] + ' altura de ' + str(maior_altura))
print('O aluno mais baixo e: codigo ' + lista_codigo[pos_menor_altura] + ' altura de ' + str(menor_altura))
'''

#40
'''
estatistica_cod = []
estatistica_veiculos = []
estatistica_acidentes = []

cont = 0
soma = 0

estatistica_cod.append('001')
estatistica_veiculos.append(1000)
estatistica_acidentes.append(30)

estatistica_cod.append('002')
estatistica_veiculos.append(10000)
estatistica_acidentes.append(120)

estatistica_cod.append('003')
estatistica_veiculos.append(6600)
estatistica_acidentes.append(12)

estatistica_cod.append('004')
estatistica_veiculos.append(300)
estatistica_acidentes.append(9)

estatistica_cod.append('005')
estatistica_veiculos.append(200000)
estatistica_acidentes.append(110)

maior_indice_acidentes = max(estatistica_acidentes)
pos_maior_indice_acidentes = estatistica_acidentes.index(maior_indice_acidentes)

menor_indice_acidentes = min(estatistica_acidentes)
pos_menor_indice_acidentes = estatistica_acidentes.index(menor_indice_acidentes)

media_veiculos = sum(estatistica_veiculos) / len(estatistica_veiculos)

for veiculos in estatistica_veiculos:
    if veiculos < 2000:
        cont += 1
        pos_veiculo = estatistica_veiculos.index(veiculos)
        soma += estatistica_acidentes[pos_veiculo]

print('Maio indice de acidente foi de ' + str(maior_indice_acidentes) + ' acidentes na cidade ' + estatistica_cod[pos_maior_indice_acidentes])
print('Menor indice de acidente foi de ' + str(menor_indice_acidentes) + ' acidentes na cidade ' + estatistica_cod[pos_menor_indice_acidentes])
print('Media de veiculos nas 5 cidades', media_veiculos)
print('Media de acidentes nas cidades com menos de 2000 veiculos', soma / cont)
'''

#41


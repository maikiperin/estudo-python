import math

#1
'''
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('O numero maior e', numero1)
#elif numero1 < numero2:
    print('O numero maior e', numero2)
#else:
    print('Os dois numeros sao iguais')
'''

#2
'''
numero = float(input('Digite o primeiro numero: '))

if numero >= 0:
    print('O numero digitado e positivo')
else:
    print('O numero digitado e negativo')
'''

#3
'''
letra = input('Digite uma letra: ')

if letra == 'M':
    print('M-Masculino')
elif letra == 'F':
    print('F-Feminino')
else:
    print('Sexo invalido')
'''

#4
'''
vogais = 'aeiou'

letra = input('Digite uma letra: ')

if letra.lower() in vogais:
    print('A letra digitada e uma vogal')
else:
    print('A letra digitada e uma consoante')
'''

#5
'''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = round((nota1 + nota2) / 2, 2)

if media == 10:
    print('Aprovado com distincao')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
'''

#6
'''
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print('O maior numero e o primeiro')
elif numero2 > numero1 and numero2 > numero3:
    print('O maior numero e o segundo')
else:
    print('O maior numero e o terceiro')
'''

#7
'''
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))

maior = 0
menor = 0

if numero1 > numero2:
    if numero1 > numero3:
        maior = numero1
    else:
        if numero3 > numero2:
            maior = numero3
        else:
            maior = numero2
else:
    if numero1 > numero3:
        maior = numero1
    else:
        if numero3 > numero2:
            maior = numero3
        else:
            maior = numero2


if numero1 < numero2:
    if numero1 < numero3:
        menor = numero1
    else:
        if numero3 < numero2:
            menor = numero3
        else:
            menor = numero2
else:
    if numero1 < numero3:
        if numero3 < numero2:
            menor = numero3
        else:
            menor = numero2
    else:
        if numero3 < numero2:
            menor = numero3
        else:
            menor = numero2

print('O maior numero e', maior)
print('O menor numero e', menor)
'''

#8
'''
preco1 = float(input('Digite o preco do primeiro produto: '))
preco2 = float(input('Digite o preco do segundo produto: '))
preco3 = float(input('Digite o preco do terceiro produto: '))

if preco1 < preco2:
    if preco1 < preco3:
        menor = preco1
    else:
        if preco3 < preco2:
            menor = preco3
        else:
            menor = preco2
else:
    if preco1 < preco3:
        if preco3 < preco2:
            menor = preco3
        else:
            menor = preco2
    else:
        if preco3 < preco2:
            menor = preco3
        else:
            menor = preco2

print('O produto mais barato e o', menor)
'''

#9
'''
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
    if numero2 > numero3:
        print(numero2)
        print(numero3)
    else:
        print(numero3)
        print(numero2)
elif numero1 > numero2 and numero1 < numero3:
    print(numero3)
    print(numero1)
    print(numero2)
elif numero1 < numero2 and numero1 > numero3:
    print(numero2)
    print(numero1)
    print(numero3)
elif numero1 < numero2 and numero1 < numero3:
    if numero2 > numero3:
        print(numero2)
        print(numero3)
    else:
        print(numero3)
        print(numero2)
    print(numero1)
'''

#10
'''
turno = input('Qual turno voce estuda (M-Matutino; V-Vespertino; N-Noturno): ')
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
else:
    print('Boa noite!')
'''

#11
'''
salario = float(input('Informe seu salario: '))
perc_reajuste = None

if salario < 280:
    perc_reajuste = 20
elif salario >= 280 and salario <= 700:
    perc_reajuste = 15
elif salario >= 700 and salario <= 1500:
    perc_reajuste = 10
elif salario > 1500:
    perc_reajuste = 5

aumento = salario * (perc_reajuste / 100)
novo_salario = salario + aumento

print('O salario antes do reajuste', salario)
print('O percentual de aumento aplicado', perc_reajuste)
print('O valor do aumento', aumento)
print('Novo salario', novo_salario)
'''

#12
'''
ganho_hora = float(input('Informe o valor por hora trabalhada: '))
horas_trabalhadas = float(input('Quantas horas trabalhou no mês: '))
salario_bruto = ganho_hora * horas_trabalhadas
perc_ir = None

if salario_bruto <= 900:
    perc_ir = 1
elif salario_bruto > 900 and salario_bruto <= 1500:
    perc_ir = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    perc_ir = 10
elif salario_bruto > 2500:
    perc_ir = 20

valor_ir = salario_bruto * (perc_ir / 100)
valor_inss = salario_bruto * (10 / 100)
valor_sindicato = salario_bruto * (3 / 100)
salario_liquido = salario_bruto - valor_ir - valor_sindicato
print('+ Salario Bruto: R$', salario_bruto)
print('- IR ('+ str(perc_ir) +'%): R$' + str(valor_ir))
print('- INSS (8%): R$', valor_inss)
print('- Sindicato (3%): R$', valor_sindicato)
print('= Salario Liquido: R$', salario_liquido)
'''

#13
'''
dia_semana = int(input('Informe o numero corresponde ao dia da semana: '))

if dia_semana == 1:
    print('1 - Domingo')
elif dia_semana == 2:
    print('2 - Segunda-feira')
elif dia_semana == 3:
    print('3 - Terça-feira')
elif dia_semana == 4:
    print('4 - Quarta-feira')
elif dia_semana == 5:
    print('5 - Quinta-feira')
elif dia_semana == 6:
    print('6 - Sexta-feira')
elif dia_semana == 7:
    print('7 - Sabado')
else:
    print('Valor invalido')
'''

#14
'''
nota1 = float(input('Informa a nota 1: '))
nota2 = float(input('Informa a nota 2: '))

media = (nota1 + nota2) / 2

resultado = None

if media > 9 and media <= 10:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
elif media >= 0 and media < 4:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    resultado = 'APROVADO'
else:
    resultado = 'REPROVADO'

print('Nota 1', nota1)
print('Nota 2', nota2)
print('A media foi', media)
print('Conceito obtido', conceito)
print('Resultado', resultado)
'''

#15
'''
lado1 = float(input('Informe o lado 1: '))
lado2 = float(input('Informe o lado 2: '))
lado3 = float(input('Informe o lado 3: '))

if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
    print('Se trata de um triangulo')
else:
    print('Não se trata de um triangulo')

if lado1 == lado2 and lado2 == lado3:
    print('Trinagulo equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Trinagulo isosceles')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Trinagulo escaleno')
'''

#16
'''
a = float(input('Informe a: '))
if a == 0:
    print('A equacao nao sera de 2 grau, programa cancelado.')
else:
    b = float(input('Informe b: '))
    c = float(input('Informe c: '))
    delta = (b ** 2) - (4 * a * c)
    print('Delta:', delta)
    if delta < 0:
        print('A equacao nao possui raizes reais')
    elif delta == 0:
        x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        print('x1:', x1)
    else:
        x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        x2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print('x1:', x1)
        print('x2:', x2)
'''

#17
'''
ano = int(input('Digite o ano a ser verificado: '))

if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    print('O ano informado e bissexto')
else:
    print('O ano informado nao e bissexto')
'''

#18
'''
data = input('Informe uma data no formato dd/mm/aaaa: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])
valida = False

# Meses com 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        valida = True
# Meses com 30 dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        valida = True
elif mes == 2:
    # Testa se é bissexto
    if (ano % 4 == 0 and ano % 400 !=0) or (ano % 400 == 0):
        if dia <= 29:
            valida = True
    elif dia <= 28:
            valida = True

if valida:
    print('Data valida')
else:
    print('Data invalida')
'''

#19
'''
numero = int(input('Digite um numero inteiro: '))

dezenas = 0
centenas = 0
unidades = 0
texto_centenas = ''
texto_dezenas = ''
texto_unidades = ''
texto_final = None

if numero / 100 >= 1:
    centenas = int(numero / 100)
    if centenas > 1:
        texto_centenas = str(centenas) + ' centenas'
    elif centenas == 1:
        texto_centenas = str(centenas) + ' centena'

if numero / 10 >= 1:
    dezenas = int((numero - (centenas * 100)) / 10)
    if dezenas > 1:
        texto_dezenas = str(dezenas) + ' dezenas'
    elif dezenas == 1:
        texto_dezenas = str(dezenas) + ' dezena'

if numero / 1 >= 1:
    unidades = int((numero - ((centenas * 100) + dezenas * 10)) / 1)
    if unidades > 1:
        texto_unidades = str(unidades) + ' unidades'
    elif unidades == 1:
        texto_unidades = str(unidades) + ' unidade'

if texto_centenas != '' and texto_dezenas != '' and texto_unidades != '':
    texto_final = texto_centenas + ', ' + texto_dezenas + ' e ' + texto_unidades
elif texto_centenas != '' and texto_dezenas != '' and texto_unidades == '':
    texto_final = texto_centenas + ' e ' + texto_dezenas
elif texto_centenas != '' and texto_dezenas == '' and texto_unidades != '':
    texto_final = texto_centenas + ' e ' + texto_unidades
elif texto_centenas != '' and texto_dezenas == '' and texto_unidades == '':
    texto_final = texto_centenas
elif texto_centenas == '' and texto_dezenas != '' and texto_unidades != '':
    texto_final = texto_dezenas + ' e ' + texto_unidades
elif texto_centenas == '' and texto_dezenas == '' and texto_unidades != '':
    texto_final = texto_unidades
elif texto_centenas == '' and texto_dezenas != '' and texto_unidades == '':
    texto_final = texto_dezenas

print(texto_final)
'''

#20
'''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = round((nota1 + nota2 + nota3) / 3, 2)

if media == 10:
    print('Aprovado com distincao')
elif media >= 7:
    print('Aprovado com a media', media)
elif media < 7:
    print('Reprovado com a media', media)
'''

#21
'''
idem 19
'''

#22
'''
numero = int(input('Informe um numero: '))

resto = numero % 2

if resto == 0:
    print('O numero digitado e par')
else:
    print('O numero digitado e impar')
'''

#23
'''
numero = float(input('Informe um numero: '))

if (numero // 1 == numero):
    print('O numero digitado e inteiro')
else:
    print('O numero digitado e decimal')
'''

#24
'''
idem a anteriores
'''

#25
'''
pergunta1 = input('Telefonou para a vítima (S/N)? ')
pergunta2 = input('Esteve no local do crime (S/N)? ')
pergunta3 = input('Mora perto da vítima (S/N)? ')
pergunta4 = input('Devia para a vítima (S/N)? ')
pergunta5 = input('Já trabalhou com a vítima (S/N)? ')

resp_sim = 0
resp_nao = 0

if pergunta1 == 'S':
    resp_sim += 1
else:
    resp_nao += 1

if pergunta2 == 'S':
    resp_sim += 1
else:
    resp_nao += 1

if pergunta3 == 'S':
    resp_sim += 1
else:
    resp_nao += 1

if pergunta4 == 'S':
    resp_sim += 1
else:
    resp_nao += 1

if pergunta5 == 'S':
    resp_sim += 1
else:
    resp_nao += 1

if resp_sim == 2:
    print('Suspeita')
elif resp_sim >= 3 and resp_sim <= 4:
    print('Cumplice')
elif resp_sim == 5:
    print('Aasassino')
'''

#26
'''
litros = float(input('Informe a litragem: '))
combustivel = input('Tipo e combustivel A-Alcool G-Gasolina: ')

preco_gasolina = 2.50
preco_alcool = 1.90
apagar = 0

if litros <= 20:
    if combustivel == 'A':
        apagar = (litros * preco_alcool) - ((litros * preco_alcool) * 0.03)
    else:
        apagar = (litros * preco_gasolina) - ((litros * preco_gasolina) * 0.04)
else:
    if combustivel == 'A':
        apagar = (litros * preco_alcool) - ((litros * preco_alcool) * 0.05)
    else:
        apagar = (litros * preco_gasolina) - ((litros * preco_gasolina) * 0.06)

print('Valor a ser pago', apagar)
'''

#27
'''
qtde_morango = float(input('Digite a quantidade (kg) de morango: '))
qtde_macas = float(input('Digite a quantidade (kg) de macas: '))

sub_morango = 0
sub_macas = 0
total = 0

if qtde_morango <= 5:
    sub_morango = qtde_morango * 2.5
else:
    sub_morango = qtde_morango * 2.2

if qtde_macas <= 5:
    sub_macas = qtde_macas * 1.8
else:
    sub_macas = qtde_macas * 1.5

print('Subtotal morango:', round(sub_morango, 2))
print('Subtotal macas:', round(sub_macas, 2))

total = sub_macas + sub_morango

if total > 25:
    print('Desconto acima de R$ 25,00: ', str(round(total * 10 / 100, 2)))
    print('')
    print('Valor a ser pago e ' + str(round(total - (total * 10 / 100), 2)))
else:
    print('Valor a ser pago e', round(total, 2))
'''

#28
#idem 27
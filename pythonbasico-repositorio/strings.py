#1
'''
string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'

print('Compara duas strings')
print('String1', string1)
print('String2', string2)
print('Tamanho de' + string1 + ': ' + str(len(string1)) + ' caracteres')
print('Tamanho de' + string2 + ': ' + str(len(string2)) + ' caracteres')

if len(string1) == len(string2):
    print('As duas strings são de tamanhos iguais')
else:
    print('As duas strings são de tamanhos diferentes')

if string1 == string2:
    print('As duas strings possuem conteúdo igual')
else:
    print('As duas strings possuem conteúdo diferente')
'''

#2
'''
nome = input('Informe seu nome: ')
aux = nome.upper()
print(aux[: : -1])
'''

#3
'''
temp = input('Informe seu nome: ')
nome = temp.upper()

for aux in nome:
    print(aux)
'''

#4
'''
temp = input('Informe seu nome: ')
nome = temp.upper()
cont = 0

for aux in nome:
    cont += 1
    print(nome[0:cont])
'''

#5
'''
temp = input('Informe seu nome: ')
nome = temp.upper()
cont = len(nome)

for aux in nome:
    print(nome[0:cont])
    cont -= 1
'''

#6
'''
data = input('Informe sua data de nascimento (dd/mm/aaaa): ')
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

print('Você nasceu em ' + data[0:2] + ' de ' + mes_ext[int(data[3:5])] + ' de ' + data[len(data) - 4:len(data)])
'''

#7
'''
frase = input('Digite uma frase: ')
vogais = ['a', 'e', 'i', 'o', 'u']
espacos = 0
qtde_vogais = 0

for aux in frase:
    if aux == ' ':
        espacos += 1
    elif aux in vogais:
        qtde_vogais += 1

print('Quantidade de espaços vazios e', espacos)
print('Quantidade de vogais e', qtde_vogais)
'''

#8
'''
frase = input('Digite uma frase: ').replace(' ', '')
invertida = frase[: : -1]
cont = 0
palindromo = True

for aux in frase:
    if aux != invertida[cont]:
        palindromo = False
        break
    else:
        cont += 1

if palindromo == True:
    print('Se trata de uma palavra/frase palindromo')
else:
    print('Não se trata de uma palavra/frase palindromo')
'''

#9
'''
import re

cpf = input('Informe seu cpf (xxx.xxx.xxx-xx): ')
retorno = True

# Verifica a formatação do CPF
if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
    retorno = False

# Obtém apenas os números do CPF, ignorando pontuações
numbers = [int(digit) for digit in cpf if digit.isdigit()]

# Verifica se o CPF possui 11 números:
if len(numbers) != 11:
    retorno = False

# Validação do primeiro dígito verificador:
sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
expected_digit = (sum_of_products * 10 % 11) % 10
if numbers[9] != expected_digit:
    retorno = False

# Validação do segundo dígito verificador:
sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
expected_digit = (sum_of_products * 10 % 11) % 10
if numbers[10] != expected_digit:
    retorno = False

print(retorno)
'''

#10










#Comparações:   ==  !=  >   <   >=  <=  not
#Comparações:   and or
#Condicionais:  if  else    elif

'''
var_verdadeiro = True #Boolean
var_falso = False

if var_verdadeiro:
    print('var_verdadeiro é verdadeiro')
else:
    print('var_verdade é falso')
'''

print('Menu:\n1 = Escreve Maiki\n2 = Escreve Renata\n3 = Escreve Thayná\n')

opcao = input('Escolha sua opção: ')

if opcao == '1':
    print('Maiki')
elif opcao == '2':
    print('Renata')
elif opcao == '3':
    print('Thayná')
else:
    print('Opção inexistente')

'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa, e decide se ela está apta a entrar no Exército.
Para entrar no Exército é preciso ter mais de 18 anos 
pesar mais ou igual a 60 kilos
e medir mais ou igual a 1.70 metros
'''
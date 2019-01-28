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

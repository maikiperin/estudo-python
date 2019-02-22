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

#6
'''
cont_notas = 0
cont_alunos = 0
nota  = 0
notas = []
medias = []
nro_alunos = 0

while cont_alunos < 5:
    cont_alunos += 1
    cont_notas = 0
    while cont_notas < 4:
        cont_notas += 1
        nota = float(input('Digite a nota ' + str(cont_notas) + ' para o aluno ' + str(cont_alunos) + ': '))
        notas.append(nota)
    medias.append(sum(notas) / len(notas))
    print('')

print(medias)

for media in medias:
    if media >= 7:
        nro_alunos += 1

print('O numero de alunos com media maior ou igual a 7 e', nro_alunos)
'''

#7
'''
vetor = [1, 2, 3, 4, 5]
multiplicacao = 1

for numero in vetor:
    multiplicacao *= numero

print('Soma dos numeros e ', sum(vetor))
print('Multiplicação dos numeros e', multiplicacao)
'''

#8
'''
cont = 0
aux = 0
idades = []
pesos = []

while cont < 2:
    cont += 1
    idade = float(input('Informe sua idade: '))
    idades.append(idade)
    peso = float(input('Informe seu peso: '))
    pesos.append(peso)
    print('')

idades.sort(reverse=True)
pesos.sort(reverse=True)

while aux < len(idades):
    print('Idade igual a ' + str(idades[aux]) + ' e peso igual a ' + str(pesos[aux]))
    aux += 1
'''

#9
'''
vetor = [1, 3, 6, 4, 5, 8, 9, 12, 7, 2]
soma = 0

for numero in vetor:
    soma += numero ** 2

print('A soma dos quadrados dos numeros do vertor e', soma)
'''

#10
'''
vetor1 = [1, 3, 5, 7, 9]
vetor2 = [2, 4, 6, 8, 10]
vetor3 = []

for num1 in vetor1:
    vetor3.append(num1)
    nposnum1 = vetor1.index(num1)
    vetor3.append(vetor2[nposnum1])

print(vetor3)
'''

#11
#idem10

#12
'''
idades = [16, 28, 18, 12, 34]
alturas = [1.76, 1.98, 1.69, 1.65, 1.87]
media_altura = sum(alturas) / len(alturas)
cont = 0

for altura in alturas:
    if altura < media_altura:
        nposaltura = alturas.index(altura)
        if idades[nposaltura] > 13:
            cont += 1

print('O numero de alunos com mais de 13 anos com altura infereior a media ' + str(round(media_altura, 2)) + ' e ' + str(cont))
'''

#13
'''
cont = 0
meses = ['1 - Janeiro', '2 - Fevereiro', '3 - Marco', '4 - Abril', '5 - Maio', '6 - Junho', '7 - Julho', '8 - Agosto', '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']
temperaturas = []

while cont < 12:
    temperatura = float(input('Infome a media da temperatura em ' + meses[cont] + ': '))
    temperaturas.append(temperatura)
    cont += 1

media_temp = sum(temperaturas) / len(temperaturas)

for temperatura in temperaturas:
    if temperatura > media_temp:
        postemp = temperaturas.index(temperatura)
        print('Temperatura acima da media [' + str(media_temp) + ']: ' + str(temperatura) + ' ocorrida no mes de ' + meses[postemp])
'''

#14
'''
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
respostas = []

for pergunta in perguntas:
    resp = input(pergunta + ': ')
    respostas.append(resp)

if respostas.count('S') == 2:
    print('Suspeita')
elif respostas.count('S') >= 3 and respostas.count('S') <= 4:
    print('Cumplice')
elif respostas.count('S') == 5:
    print('Assassino')
else:
    print('Inocente')
'''

#15
'''
notas = []

while True:
    nota = float(input('Informa uma nota Ou -1 para encerrar o programa: '))
    if nota == -1:
        break
    else:
        notas.append(nota)


print('Quantidade de valores que foram lidos', len(notas))
print(notas)

notas.sort(reverse=True)

print(notas)
print(sum(notas))
print(sum(notas) / len(notas))
print('')
print('Fim do programa!')
'''

#16
#???

#17
'''
atleta = input('Digite o nome do atleta: ')

tipos_saltos = ['Primeiro Salto', 'Segundo Salto', 'Terceiro Salto', 'Quarto Salto', 'Quinto Salto']

saltos = []
cont = 0
saltos_sep = ''

while cont < 5:
    salto = float(input('Informe o ' + tipos_saltos[cont] + ': '))
    saltos.append(salto)
    cont += 1

print('')
print('Atleta:', atleta)
print('')

for aux in saltos:
    pos_salto = saltos.index(aux)
    print(tipos_saltos[pos_salto] + ': ' + str(aux) + ' m')
    if pos_salto != 4:
        saltos_sep = saltos_sep + str(aux) + ' - '
    else:
        saltos_sep = saltos_sep + str(aux)

print('Resultado Final:')
print('Atleta:', atleta)
print('Saltos: ' + str(saltos_sep))
print('Media dos saltos ' + str(round(sum(saltos) / len(saltos), 1)) + ' m')
'''

#18
'''
numeros = []
cont = 0
qtde_votos = 0

maior_votos = 0
maior_qtde = 0
maior_perc = 0

print('Enquete: Quem foi o melhor jogador?\n')

while True:
    numero = int(input('Número do jogador (0=fim): '))
    if numero == 0:
        break
    elif numero < 1 or numero > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    else:
        numeros.append(numero)

print('\nResultado da votação:\n')
print('Foram computados ' + str(len(numeros)) + ' votos.\n')
print('Jogador\t\t\t\tVotos\t\t\t\t%')

while cont < 23:
    qtde_votos = numeros.count(cont)
    if qtde_votos > 0:
        print(str(cont) + '\t\t\t\t\t' + str(qtde_votos) + '\t\t\t\t\t' + str(round((qtde_votos / len(numeros) * 100), 1)) + '%')
    if qtde_votos > maior_qtde:
        maior_votos = cont
        maior_qtde = qtde_votos
        maior_perc = round((qtde_votos / len(numeros) * 100), 1)
    cont += 1

print('o melhor jogador foi o ' + str(maior_votos) + ', com ' + str(maior_qtde) + ' votos, correpondendo a ' + str(maior_perc) + '% do total de votos.')
'''

#19
#idem 18

#20
'''
salarios = []
salario = 0
abonos = []
abono = 0
minimos = []

while True:
    salario = float(input('Salário: '))
    if salario == 0:
        break
    else:
        salarios.append(salario)
        abono = salario * 0.2
        if abono <= 100:
            abono = 100
            minimos.append(abono)
        abonos.append(abono)

print('\nSalário\t\t- Abono')

for imp in salarios:
    pos_abono = salarios.index(imp)
    print('R$ {:.2f}'.format(imp) + ' \t- R$ {:.2f}'.format(abonos[pos_abono]))

print('\nForam processados ' + str(len(salarios)) + ' colaboradores')
print('Total gasto com abono: R$ {:.2f}'.format(sum(abonos)))
print('Valor mínimo pago a ' + str(len(minimos)) + ' colaboradores')
print('Maior valor de abono pago: R$ {:.2f}'.format(max(abonos)))
'''

#21
'''
cont = 0

veiculos = ['C4', 'UP', 'UNO']
kms = [8.2, 9.0, 10.3]

print('Comparativo de Consumo de Combustível')

for veiculo in veiculos:
    cont += 1
    print('Veiculo', cont)
    print('Nome:', veiculo)
    pos_veiculo = veiculos.index(veiculo)
    print('Km por litro:', kms[pos_veiculo])

print('\nRelatório Final')

cont = 0

for veiculo in veiculos:
    cont += 1
    pos_veiculo = veiculos.index(veiculo)
    print(str(cont) + ' - ' + veiculo + '\t\t\t\t' + str(kms[pos_veiculo]) + ' - ' + str(round(1000 / kms[pos_veiculo], 1)) + ' litros - R$ {:.2f}'.format(round(1000 / kms[pos_veiculo], 1) * 2.25))

menor_consumo = max(kms)
pos_consumo = kms.index(menor_consumo)
print('O menor consumo é do', veiculos[pos_consumo])
'''

#22
'''
mouses = []
defeitos = []

tipos_defeitos = []
cont = 0
qtde_defeitos = 0
percentual = 0

while True:
    mouse = int(input('Informe o numero do mouse: '))
    if mouse == 0:
        break
    else:
        mouses.append(mouse)
        defeito = input('Informe o defeito do mouse: ')
        defeitos.append(defeito)

print('\nQuantidade de mouses:', len(mouses))
print('\nSituação\t\t\t\t\t\tQuantidade\t\t\t\t\tPercentual')

for tipo_defeito in defeitos:
    if defeitos.count(tipo_defeito) > 0:
        if tipos_defeitos.count(tipo_defeito) == 0:
            tipos_defeitos.append(tipo_defeito)

for aux in tipos_defeitos:
    cont += 1
    qtde_defeitos = defeitos.count(aux)
    percentual = round((qtde_defeitos / len(defeitos)) * 100, 2)
    print(str(cont) + ' - ' + aux + '\t\t\t\t\t' + str(qtde_defeitos) + '\t\t\t\t\t' + str(percentual))
'''

#23
'''
funcionarios = ['alexandre       ', 'anderson        ', 'antonio         ', 'carlos          ', 'cesar           ', 'rosemary        ']
espaco_disco = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]
cont = 0
total = 0

print('ACME Inc.\t\t\t\t\tUso do espaço em disco pelos usuários')
print('--------------------------------------------------------------------')
print('Nr.\t\tUsuário\t\t\t\tEspaço utilizado\t\t% do uso')
print('')

for funcionario in funcionarios:
    cont += 1
    posfunc = funcionarios.index(funcionario)
    perc = round((espaco_disco[posfunc] / sum(espaco_disco)) * 100, 2)
    print(str(cont) + '\t\t' + funcionario + '\t' + str(round((espaco_disco[posfunc] / 1024) / 1024, 2)) + ' MB\t\t\t\t' + str(perc))
    total += round((espaco_disco[posfunc] / 1024) / 1024, 2)

print('\nEspaço total ocupado: ' + str(total) + ' MB')
print('Espaço médio ocupado: ' + str(round(total / len(funcionarios) ,2)) + ' MB')
'''

#24

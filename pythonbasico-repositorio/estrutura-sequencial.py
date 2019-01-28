#1
#mensagem = 'Alo mundo'
#print(mensagem)

#2
#numero = input('Digite um numero: ')
#print('O número informado foi', numero)

#3
#numero1 = input('Digite o primeiro numero: ')
#numero2 = input('Digite o segundo numero: ')
#print('A soma dos doi numeros informados e', int(numero1) + int(numero2))

#4
#nota1 = float(input('Informe a nota 1: '))
#nota2 = float(input('Informe a nota 2: '))
#nota3 = float(input('Informe a nota 3: '))
#nota4 = float(input('Informe a nota 4: '))
#print('A media das notas foi', (nota1 + nota2 + nota3 + nota4) / 4)

#5
#medida = float(input('Informe uma medidade em metros: '))
#centimetro = medida * 100
#print('A medida informada corresponde a ' + str(centimetro) + ' centimetros')

#6
''' Para calcular a área do círculo devemos utilizar a seguinte fórmula:
A = π . r2
Onde,

π: constante Pi (3,14)
r: raio
'''

#raio = float(input('Informe o raio do circulo: '))
#area = 3.14 * (raio**2)
#print('A area do circulo e ', area)

#7
#Calcular area do quadrado: L * L
#medida = float(input('Informe a medida de um lado do quadrado: '))
#area = (medida**2) * 2
#print('O dobro da area do quadrado e', area)

#8
#ganho_hora = float(input('Informe o valor por hora trabalhada: '))
#horas_trabalhadas = float(input('Quantas horas trabalhou no mês: '))
#salario = ganho_hora * horas_trabalhadas
#print('O salario deste mes sera R$', salario)

#9
#Tranformar graus farenheit em graus celsius
# C = (5 * (F-32) / 9)
#temp_f = float(input('Informe a temperatura em farenheit: '))
#temp_c = (5 * (temp_f - 32) / 9)
#print('A temperatura correspondente em graus celsius e', round(temp_c, 0))

#10
#Tranformar graus celsius em graus farenheit
# F = C * 1.8 + 32
#temp_c = float(input('Informe a temperatura em celsius: '))
#temp_f = temp_c * 1.8 + 32
#print('A temperatura correspondente em graus farenheit e', round(temp_f, 0))

#11
#numero1 = int(input('Digite o primeiro numero: '))
#numero2 = int(input('Digite o segundo numero: '))
#numero3 = float(input('Digite o terceiro numero: '))

#a = (numero1 * 2) * (numero2 / 2)
#b = (numero1 * 3) + numero3
#c = numero3 ** 3

#print('O produto do dobro do primeiro com metade do segundo', a)
#print('A soma do triplo do primeiro com o terceiro', b)
#print('O terceiro elevado ao cubo', c)

#12
#altura = float(input('Digite sua altura: '))
#peso_ideal = (72.7 * altura) - 58
#print('Seu peso ideal e', peso_ideal)

#13
#altura = float(input('Digite sua altura: '))
#sexo = input('Digite seu sexo (m/f): ')

#if sexo == 'm':
#    peso_ideal = (72.7 * altura) - 58
#else:
#    peso_ideal = (62.1 * altura) - 44.7

#print('Seu peso ideal e', peso_ideal)

#14
#peso_peixes = float(input('Digite o peso (kg) dos peixes: '))

#if peso_peixes > 50:
#    excesso = peso_peixes - 50
#    multa = excesso * 4
#    print('De acordo com o limite de peso de peixes (50 kg) o excesso foi ' + str(excesso) + ', gerando uma multa no valor de R$ ' + str(multa))

#else:
#    print('Peso dentro da regra de excesso')

#15
#ganho_hora = float(input('Informe o valor por hora trabalhada: '))
#horas_trabalhadas = float(input('Quantas horas trabalhou no mês: '))
#salario_bruto = ganho_hora * horas_trabalhadas
#valor_ir = salario_bruto * (11 / 100)
#valor_inss = salario_bruto * (8 / 100)
#valor_sindicato = salario_bruto * (5 / 100)
#salario_liquido = salario_bruto - valor_ir - valor_inss - valor_sindicato
#print('+ Salario Bruto: R$', salario_bruto)
#print('- IR (11%): R$', valor_ir)
#print('- INSS (8%): R$', valor_inss)
#print('- Sindicato (5%): R$', valor_sindicato)
#print('= Salario Liquido: R$', salario_liquido)

#16
#area = float(input('Informa o tamanho em metros quadrados da área a ser pintada: '))
#litros = area / 3
#latas = litros / 18
#total = round(latas, 0) * 80

#print('Quantidade de latas a serem compradas', round(latas, 0))
#print('Preço total R$', round(total, 2))

#17
#area = float(input('Informa o tamanho em metros quadrados da área a ser pintada: '))
#litros = area / 6
#latas = litros / 18
#galoes = litros / 3.6
#total_latas = round(latas, 0) * 80
#total_galoes = round(galoes, 0) * 25

#print('Quantidade de latas a serem compradas', round(latas, 0))
#print('Preço total somente latas R$', round(total_latas, 2))

#print('Quantidade de galoes a serem comprados', round(galoes, 0))
#print('Preço total somente galoes R$', round(total_galoes, 2))

#18
#tamanho_arquivo = float(input('Informa o tamanho (MB) do arquivo : '))
#velocidade_link = float(input('Informa a velocidade (Mbps) do arquivo : '))
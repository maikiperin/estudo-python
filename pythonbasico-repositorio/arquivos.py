#1
'''
import sys,socket

ip_validos = []
ip_invalidos = []

arq_ent = open('c:\\temp\\enderecos_ip.txt',  'r')

for ip in arq_ent:
    try:
        socket.inet_aton(ip)
        ip_validos.append(ip)
    except socket.error:
        ip_invalidos.append(ip)

arq_saida = open('c:\\temp\\relatorio.txt',  'w')

arq_saida.write('[Endereços válidos:]\n')
for aux in ip_validos:
    arq_saida.write(aux)

arq_saida.write('\n[Endereços inválidos:]\n')
for aux in ip_invalidos:
    arq_saida.write(aux)
'''

#2

arq_ent = open('c:\\temp\\usuarios.txt',  'r')

dados = []
cont = 0
total = 0

for linha in arq_ent:
    cont += 1
    dados.append(linha.split())
print(dados)
#perc = round((espaco_disco[posfunc] / sum(espaco_disco)) * 100, 2)
#total += round((espaco_disco[posfunc] / 1024) / 1024, 2)

'''
arq_saida = open('c:\\temp\\rel_usuarios.txt',  'w')

arq_saida.write('ACME Inc.\t\t\t\t\tUso do espaço em disco pelos usuários')
arq_saida.write('\n--------------------------------------------------------------------')
arq_saida.write('\nNr.\t\tUsuário\t\t\t\tEspaço utilizado\t\t% do uso')
arq_saida.write('\n')

print(str(cont) + '\t\t' + funcionario + '\t' + str(round((espaco_disco[posfunc] / 1024) / 1024, 2)) + ' MB\t\t\t\t' + str(perc))

arq_saida.write('\nEspaço total ocupado: ' + str(total) + ' MB')
arq_saida.write('\nEspaço médio ocupado: ' + str(round(total / len(funcionarios) ,2)) + ' MB')
'''
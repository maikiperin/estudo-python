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
'''
def ret_perc(valor, total):
    return round((valor / total) * 100, 2)

def ret_mb(valor):
    return round((valor / 1024) / 1024, 2)

arq_ent = open('c:\\temp\\usuarios.txt',  'r')

dados = []
cont = 0
total = 0

for linha in arq_ent:
    dados.append(linha.split())

dados = [[i[0].ljust(15), int(i[1])] for i in dados]

for espaco in dados:
    total += espaco[1]

arq_saida = open('c:\\temp\\rel_usuarios.txt', 'w')

arq_saida.write('ACME Inc.\t\t\t\t\tUso do espaço em disco pelos usuários')
arq_saida.write('\n--------------------------------------------------------------------')
arq_saida.write('\nNr.\t\tUsuário\t\t\t\tEspaço utilizado\t\t% do uso')
arq_saida.write('\n')

for ocupacao in dados:
    cont += 1
    percentual = ret_perc(ocupacao[1], total)
    espaco_mb = ret_mb(ocupacao[1])
    arq_saida.write('\n' + str(cont) + '\t\t' + ocupacao[0] + '\t\t' + str(espaco_mb).rjust(10) + ' MB\t\t\t\t' + str(percentual) + '%')

arq_saida.write('\n\nEspaço total ocupado: ' + str(ret_mb(total)) + ' MB')
arq_saida.write('\nEspaço médio ocupado: ' + str(ret_mb(total / cont)) + ' MB')
'''
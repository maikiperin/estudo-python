#open('arquivo.txt',  'r+')

'''
Abertura de arquvivos textos, opções:
O default é 'r' (read)
'w' (write), cria o arquivo se o mesmo não existir, e se o mesmo existir apaga o conteúdo do arquivo 
'r+' (read + write)
'a' (appnend), cria o arquivo se o mesmo não existir, e adiciona se o mesmo existir

Abertura de arquivos binários (imagens, vídeos, etc.), opções:
'b' (bytes)
'rb' (read + bytes)
'''

arquivo = open('arquivo.txt',  'w')

for i in range(1, 101):
    arquivo.write('Numero: ' + str(i) + '\n')

arquivo = open('arquivo.txt',  'r')

print(arquivo.read())

arqimg = open('logo.png',  'rb')

print(arqimg.read())


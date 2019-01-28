import time

try:
    a = 1200 / 0
except:
    print('Erro! Divisão por zero.')

print('o programa continua...')

try:
    a = 1200 / 0
except ZeroDivisionError:
    print('Erro! Divisão por zero.')

try:
    funcaoquenaoexiste()
except ZeroDivisionError:
    print('Erro! Divisão por zero.')
except NameError:
    print('Você digitou alguma coisa errada.')

try:
    funcaoquenaoexiste()
except Exception as erro:
    print('Erro:', erro)

def abre_arquivo():
    try:
        open('arquivoquenaoexiste.txt')
        return True
    except Exception as erro:
        print('Erro:', erro)
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo...')
    time.sleep(5)

print('Abriu o arquivo')
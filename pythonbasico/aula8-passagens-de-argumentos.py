import sys

argumentos = sys.argv       # arqu1 method / arrq2 n1 / arq3 n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)
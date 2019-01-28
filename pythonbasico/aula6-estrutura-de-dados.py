minha_tupla = ('João', 'Maria')                     # TUPLA (tuple)
meu_dicionario = {'nome': 'Maiki', 'idade': 38}     # DICIONARIO (dict)
meu_conjunto = {'Maiki', 'João'}                    # CONJUNTO (set)

print(minha_tupla)
print(type(minha_tupla))
print(minha_tupla[0])

for nome in minha_tupla:
    print(nome)

minha_tupla = ('Maria', 'Joaquim')
print(minha_tupla)

if 'Maria' in minha_tupla:
    print('Maria está na minha_tupla')

print(meu_dicionario)
print(meu_dicionario['nome'])
print(len(meu_dicionario))

if 'Maiki' in meu_dicionario.values():
    print('Maiki está no meu_dicionario')

for valores in meu_dicionario.values():
    print(valores)

for valores in meu_dicionario.keys():
    print(valores)

meu_dicionario['nome'] = 'Renata'
print(meu_dicionario)

meu_dicionario['endereco'] = 'Rua MDV 6, Qd. 36 Lt. 16, casa 02'
print(meu_dicionario)

print(meu_conjunto)

meu_conjunto.add('Maria')
print(meu_conjunto)

meu_conjunto.add('Maiki')   #já tinha, então o python desconsidera
print(meu_conjunto)

if 'Maiki' in meu_conjunto:
    print('Maiki foi enconrato no meu_conjunto')

# Inicialização de variáveis
lista = []
tupla = ()
dicionario = {}     # ou dict()
conjunto = set()
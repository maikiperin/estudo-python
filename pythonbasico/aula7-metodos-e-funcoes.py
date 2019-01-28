def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

# Função localizada na web
def arredondar(num):
    return float( '%g' % ( num ) )

retorno = soma(1, 2)
print(retorno)

retorno2 = arredondar(soma(1.1, 2.2))
print(retorno2)

def imprime_Ola_Mundo():
    print('Ola Mundo!')

imprime_Ola_Mundo()

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print(tem_sete_itens('oi pessoal'))
print(tem_sete_itens('1234567'))

if tem_sete_itens('1234567'):
    print('Realmente tem 7 itens')

'''
EXERCICIO: Escreva uma função que receba um objeto de coleção (lista, conjunto, tupla, etc.) 
e retorna o valor do maior número dentro dessa coleção
Faça outra função que retorne o menor número dessa coleção
'''

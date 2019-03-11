'''
from classes import Quadrado

meu_quadrado = Quadrado(4)
print(meu_quadrado.tamanho_lado)
print(meu_quadrado.retValorLado())
print(meu_quadrado.calculaArea())
'''

'''
from classes import Retangulo

base = int(input('Informe o comprimento base: '))
altura = int(input('Informe o comprimento da altura: '))

meu_retangulo = Retangulo(base, altura)

print(str(meu_retangulo.calculaPerimetro()) + ' pisos')
'''

'''
from classes import Pessoa

nome = input('Digite o nome da pessoa: ')
idade = int(input('Digite a idade da pessoa: '))
peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))

minha_pessoa = Pessoa(nome, idade, peso, altura)

print(minha_pessoa.Engordar(10))
'''

'''
from classes import ContaCorrente

conta = input('Informe sua conta: ')
correntista = input('Informe seu nome: ')

minha_cc = ContaCorrente(conta, correntista)

minha_cc.Deposito(200)
minha_cc.Saque(50)
minha_cc.Deposito(10)

print('Saldo atual R$ {:.2f}'.format(minha_cc.Saldo()))
'''

'''
from classes import Tv

minhaTv = Tv()

minhaTv.alteraCanal(10)
minhaTv.aumentaVol()
minhaTv.aumentaVol()
minhaTv.aumentaVol()
minhaTv.aumentaVol()
minhaTv.aumentaVol()
minhaTv.aumentaVol()

print('Canal: ' + str(minhaTv.statusTv()[0]) + ' e voume ' + str(minhaTv.statusTv()[1]))
'''

'''
from classes import Tami

nome = input('Informe o nome do seu bichinho: ')

meu_Tami = Tami(nome)

print(meu_Tami.retHumor())
'''
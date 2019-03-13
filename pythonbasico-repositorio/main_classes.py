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

'''
from classes import Ponto
from classes import Retangulo


meu_retangulo = Retangulo(8, 10)

lista_pontos = meu_retangulo.centroRetangulo()

meu_ponto = Ponto(lista_pontos[0], lista_pontos[1])

meu_ponto.impValores()
'''

'''
from classes import Carro

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()
'''

'''
from classes import ContaInvestimento

conta = input('Informe sua conta poupança: ')
correntista = input('Informe seu nome: ')

minha_cp = ContaInvestimento(conta, correntista, 1000, 10)

minha_cp.Deposito(200)
minha_cp.Saque(50)
minha_cp.Deposito(10)
minha_cp.adicionaJuros()
minha_cp.adicionaJuros()
minha_cp.adicionaJuros()
minha_cp.adicionaJuros()
minha_cp.adicionaJuros()

print('Saldo atual R$ {:.2f}'.format(minha_cp.Saldo()))
'''
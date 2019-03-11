#1
'''
class bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocaCor(self, novacor):
        self.cor = novacor

    def mostraCor(self):
        print(self.cor)
'''

#2
'''
class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudaTamanho(self, novo_tamamnho):
        self.tamanho_lado = novo_tamamnho

    def retValorLado(self):
        return self.tamanho_lado

    def calculaArea(self):
        return self.tamanho_lado ** 2
'''
#3
'''
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudaValorBase(self, novo_valor):
        self.base = novo_valor

    def mudaValorAltura(self, novo_valor):
        self.altura = novo_valor

    def retValorBase(self):
        return self.base

    def retValorAltura(self):
        return self.altura

    def calculaArea(self):
        return self.base * self.altura

    def calculaPerimetro(self):
        return 2 * (self.base + self.altura)
'''

#4
'''
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def Engordar(self, kilos):
        self.peso += kilos

    def Emagrecer(self, kilos):
        self.peso -= kilos

    def Crescer(self, centimetros):
        self.altura += centimetros
'''

#5
'''
class ContaCorrente:
    def __init__(self, conta, correntista, saldo=0):
        self.conta = conta
        self.correntista = correntista
        self.saldo = saldo

    def alterarNome(self, novonome):
        self.correntista = novonome
        return self.correntista

    def Deposito(self, valor):
        self.saldo += valor

    def Saque(self, valor):
        self.saldo -= valor

    def Saldo(self):
        return self.saldo
'''

#6
'''
class Tv:
    def __init__(self, canal=2, volume=0):
        self.canal = canal
        self.volume = volume

    def alteraCanal(self, novocanal):
        self.canal = novocanal

    def aumentaVol(self):
        self.volume += 1

    def diminuiVol(self):
        self.volume -= 1

    def statusTv(self):
        return [self.canal, self.volume]
'''

#7
'''
class Tami:
    def __init__(self, nome, idade=1, fome="sim", saude="boa"):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alteraNome(self, novonome):
        self.nome = novonome

    def alteraForme(self, novofome):
        self.fome = novofome

    def alteraSaude(self, novasaude):
        self.saude = novasaude

    def alteraIdade(self):
        self.idade += 1

    def retNome(self):
        return self.nome

    def retFome(self):
        return self.fome

    def retSaude(self):
        return self.saude

    def retIdade(self):
        return self.idade

    def retHumor(self):
        if self.fome == 'sim' and self.saude == 'boa':
            return 'com fome'
        elif self.fome == 'sim' and self.saude == 'ruim':
            return 'fraco'
        elif self.fome == 'nao' and self.saude == 'boa':
            return 'de boa'
        elif self.fome == 'nao' and self.saude == 'ruim':
            return 'doente'
'''

#8


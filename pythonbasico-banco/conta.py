class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def sacar(self, valor):
        if self.saldo - valor < self.limite:
            print('Saldo insuficiente!')
        else:
            self.saldo -= valor

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Não é possível realizar depósito de valores negativos!')

    def consulta_saldo(self):
        return str(self.saldo)

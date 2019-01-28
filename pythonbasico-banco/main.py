from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Maiki', '04169599624', 38)
print(cliente1)

conta1 = Conta(cliente1, 100, 1000)

conta1.depositar(200)
print(conta1.consulta_saldo())

conta1.sacar(500)
print(conta1.consulta_saldo())


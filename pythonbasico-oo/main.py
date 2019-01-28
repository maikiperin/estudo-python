from veiculo import Veiculo
from carro import Carro

caminhao_preto = Veiculo('preto', 8, 'scania', 300)

print(caminhao_preto)
print(type(caminhao_preto))
print(caminhao_preto.cor)

caminhao_branco = Veiculo('branco', 8, 'ford', 400)
print(caminhao_branco.tanque)

caminhao_branco.abastecer(50)
print(caminhao_branco.tanque)

carro_prata = Carro('prata', 'ford', 65)
print(carro_prata.tanque)

carro_prata.abastecer(50)
print(carro_prata.tanque)

'''
EXERCICIO: Crie um software de gerenciamento bancário
Este software poderá ser capaz de criar clientes e contas
Cada cliente possui: nome, cpf e idade
Cada conta possui: cliente, saldo, limite e métodos sacar, depositar e consultar saldo
'''
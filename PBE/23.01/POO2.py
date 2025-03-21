# implemente uma classe chamada contaBancaria que possua atributos para armazenar o numero da conta, nome do titular e saldo. adicione metodos para realizar depositos e saques

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque deve ser positivo.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta1 = ContaBancaria(123, "João", 1000)
conta2 = ContaBancaria(456, "Maria", 500)

conta1.consultar_saldo()
conta2.consultar_saldo()

conta1.deposito(200)

conta2.saque(100)

conta1.consultar_saldo()
conta2.consultar_saldo()







    
# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio

#     def calcular_area(self):
#         return math.pi * (self.raio ** 2)

#     def calcular_perimetro(self):
#         return 2 * math.pi * self.raio
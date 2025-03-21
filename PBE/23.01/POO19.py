# 19.	Implemente uma classe chamada “JogoAdivinhacao” que represente um jogo de adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça palpites e informar se o palpite está correto, informando se é maior ou menor que o número gerado.

import random

class Jogo:
    def __init__(self):
        self.num = random.randint(1, 10)
        self.palpite_atual = None

    def jogar(self):
        while True:
            self.palpite_atual = int(input("Digite um número de 1 a 10: "))
            if self.distancia():
                break
        print("Você venceu!")

    def distancia(self):
        if self.palpite_atual > self.num:
            print("O número correto é menor.")
        elif self.palpite_atual < self.num:
            print("O número correto é maior.")
        else:
            return True 
        return False  

jogo = Jogo()
jogo.jogar()


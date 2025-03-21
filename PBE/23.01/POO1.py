# crie uma classe chamada "circulo" que possua um atributo para armazenar o raio e metodos para calcular a area e o perimetro do circulo


import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
meu_circulo = Circulo(5)
area = meu_circulo.calcular_area()
print(f"A área do círculo é: {area}")

perimetro = meu_circulo.calcular_perimetro()
print(f"O perímetro do círculo é: {perimetro}")

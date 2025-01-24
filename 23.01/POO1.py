# crie uma classe chamada "circulo" que possua um atributo para armazenar o raio e metodos para calcular a area e o perimetro do circulo


import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
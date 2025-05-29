#  crie uma classe chamada "Retangulo" que possua atributos para armazenar a largura e a altura. implemente metodos para calcular a area e o perimetro do retangulo



class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        area = self.largura * self.altura
        print(f"a area do retangulo é {area}")

    def perimetro(self):
        perimetro = (self.largura * 2) + (self.altura * 2)
        print(f"o perimetro do retangulo é {perimetro}")

resultArea = Retangulo(20, 10)
resultPerimetro = Retangulo(20, 10)

resultArea.area()
resultPerimetro.perimetro()



class carro():
    def __init__(self, marca, cor):
        
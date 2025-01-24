# crie uma classe chamada "Retangulo" que possua atributos para armazenar a largura e a altura. implemente metodos para calcular a area e o perimetro do retangulo

class retangulo:

    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area (self, retangulo):
        area_retangulo = self.largura * self.altura
        print(f"a area do retangulo é: {area_retangulo}")



    # def perimetro(self, retangulo):

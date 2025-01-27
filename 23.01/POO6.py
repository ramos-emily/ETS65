# 6.	Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def estoque(self):
        return self.preco * self.quantidade

dados_produto = Produto("Manteiga",3.99,20)
print(f"{dados_produto.estoque():.2f}")


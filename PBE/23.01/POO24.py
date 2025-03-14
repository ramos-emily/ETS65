# 24.	Desenvolva um sistema de gestão de um zoológico, com classes para Animal, Habitat, Alimentação, Veterinário, e Funcionário. Cada tipo de animal terá características específicas, como dieta e necessidades ambientais, e o sistema deve permitir o controle de alimentação, saúde e movimentação dos animais.

class Animal:
    def __init__(self, nome, especie, dieta, habitat, necessidades):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta
        self.habitat = habitat
        self.necessidades = necessidades
    
    def exibir_informacoes(self):
        print(f"Animal: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Dieta: {self.dieta}")
        print(f"Habitat: {self.habitat}")
        print(f"Necessidades: {self.necessidades}")

class Habitat:
    def __init__(self, tipo, temperatura, tamanho):
        self.tipo = tipo
        self.temperatura = temperatura
        self.tamanho = tamanho
    
    def exibir_habitat(self):
        print(f"Tipo de Habitat: {self.tipo}")
        print(f"Temperatura: {self.temperatura}")
        print(f"Tamanho: {self.tamanho}")

class Alimentacao:
    def __init__(self, tipo, quantidade, frequencia):
        self.tipo = tipo
        self.quantidade = quantidade
        self.frequencia = frequencia
    
    def exibir_alimentacao(self):
        print(f"Tipo de Alimentação: {self.tipo}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Frequência: {self.frequencia} vezes por dia")

habitat_leao = Habitat("savana", 30, 500)
alimentacao_leao = Alimentacao("carnivoro", 10, 2)
leao = Animal("miguel", "leão", "carnívoro", "savana", "grama")
    
leao.exibir_informacoes()
habitat_leao.exibir_habitat()
alimentacao_leao.exibir_alimentacao()


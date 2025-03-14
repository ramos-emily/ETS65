#Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).

class Aluno():
    def __init__(self, nome, matricula, nota1, nota2):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def mediaNotas(self):
        media = (self.nota1 + self.nota2) / 2
        if media >= 7:
            print("Passou carai!")
        elif media >= 6:
            print("Melhore")
        else:
            print("Se fudeu")

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Notas: {self.nota1}, {self.nota2}"

nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

ver = Aluno(nome, matricula, nota1, nota2)

print(ver)
ver.mediaNotas()


    
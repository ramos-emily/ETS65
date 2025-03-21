# 9.	Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas.

class Paciente:
    def __init__(self,nome,idade,historico):
        self.nome = nome
        self.idade = idade
        self.historico = historico
    
    def add_consulta(self):
        consulta = input("Que consulta quer adicionar ao histórico: ")
        self.historico.append(consulta)
        return consulta

paciente = Paciente("Gabriel", 19, ["Oftalmo", "Pediatra", "Dermato"])
paciente.add_consulta()

print(f"Histórico de consultas: {paciente.historico}")

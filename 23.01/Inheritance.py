'''======================= Herança =======================

É a capacidade de um objeto ser idealizado beseado em outro objeto, se o objeto
principal existem atributos que são "propriedades" e os métodos que são as
"funções" que eles pdoem ser extendidos para um objeto filho  
'''

class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def presentation(self):
        return f"Meu nome é {self.name} e tenho {self.age} anos!"
    
class Student(People):
    def __init__(self, name, age,registration):
        super().__init__(name, age)
        self.registration = registration

    

    def presentation(self):
        return f"Meu nome é {self.name} e tenho {self.age} anos! e estou atualmente no curso de {self.registration}"
    
people = People('Victor',19)
student = Student('Victor',19,'Desenvolvimento de Sistenas')

print(people.presentation())
print(student.presentation())
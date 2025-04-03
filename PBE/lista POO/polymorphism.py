'''======================= Polimorfismo =======================

O polimorfismo é outro conceito fundamental para programação Orientada a Objetos 
Com polimorfismo você pode usar em um método com o mesmo nome em diferentes classes,
mas cada classe pode emplementar esse método de forma destinta. Isso é util para criar 
sistemas mais flexisíveis e reutilizavéis
'''

class Dog():
    def __init__(self, name, food, sleep):
        self.name = name
        self.food = food
        self.sleeep = sleep
    
    def sniff(self, objeto_qualquer):
        self.objeto = objeto_qualquer
        return f'Farejou {self.objeto}'

    def sleep(self):
        self.sleeep = False
        return f'O {self.name} está descansado, SEXTOOU '
    
class PoliceDog(Dog):
    def __init__(self, name, food, sleep):
        super().__init__(name, food, sleep)
    
    def sniff(self, objeto_especifico):
        self.objeto = objeto_especifico
        return f'Farejou {self.objeto}'


dog_caramelo = Dog('Nelson', 'Pedigree', 2)

dog_policial = PoliceDog('Godofredo', 'Petisco', 1)

print(dog_caramelo.sniff('Meia'))
print(dog_policial.sniff('Coisas Ilícitas'))
print(dog_caramelo.sleep())
print(dog_policial.sleep())


#busca linear
#acha o indice, a posiçao que aquele numero ocupa

def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return "nao funcionou kakakakkakkaakaka"
    
lista = [5, 3, 8, 8, 2]
valor = 8
    
socorro = busca_linear(lista, valor)
print(socorro)

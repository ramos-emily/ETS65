#buscaBinaria
#Ela divide a lista ao meio, verifica o valor no meio,
#e em seguida decide qual metade da lista pode ser descartada, repetindo esse processo até encontrar o valor ou concluir que ele não existe na lista


lista = [3, 7, 12, 19, 25, 30, 35, 42, 50, 58]

def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio  
        elif lista[meio] > valor:
            fim = meio - 1 
        else:
            inicio = meio + 1
    
    return -1

valor_procurado = int(input("digite um numero: "))
resultado = busca_binaria(lista, valor_procurado)

if resultado != -1:
    print(f"Valor {valor_procurado} encontrado no índice {resultado}.")
else:
    print(f"Valor {valor_procurado} não temmmm")



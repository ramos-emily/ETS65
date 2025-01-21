def ordenar_lista(lista):
    for i in range(len(lista)):
        for num in range(i + 1, len(lista)):
            if lista[i] > lista[num]:
                lista[i], lista[num] = lista[num], lista[i]
    return lista

#Merge Sort sem usar função!!

lista = [38, 27, 43, 3, 9, 82, 10]

print("\n---------------------------------\n")
print("parte 1\n")

#dividir
#  → [38, 27, 43] e [3, 9, 82, 10]
# [38, 27, 43] → [38] e [27, 43]
# [3, 9, 82, 10] → [3, 9] e [82, 10] 

etapaUm = lista[:3]
etapaUmPontoUm = lista[3:]

print(f"{etapaUm} e {etapaUmPontoUm}")

ptUm = etapaUm[:1]
ptUmPontoUm = etapaUm[1:]

print(f"{ptUm} e {ptUmPontoUm}")

ptDois = etapaUmPontoUm[:2]
ptDoispontoDois = etapaUmPontoUm[2:]

print(f"{ptDois} e {ptDoispontoDois}")

print("\n---------------------------------\n")
print("parte 2\n")


#fusao das sublinhas pequenas, aqui voce pega as partes com mais de dois numeros e ordena em crescente
# [27, 43] se mantém [27, 43]
# [3, 9] se mantém [3, 9]
# [82, 10] se torna [10, 82]
ptDoispontoDois = ordenar_lista(ptDoispontoDois)

print(ptUmPontoUm)
print(ptDois)
print(ptDoispontoDois)

print("\n---------------------------------\n")
print("parte 3\n")


# Fusão das sublistas médias:

# [38] e [27, 43] se tornam [27, 38, 43]
# [3, 9] e [10, 82] se tornam [3, 9, 10, 82]
etapaUm = ordenar_lista(etapaUm)
etapaUmPontoUm = ordenar_lista(etapaUmPontoUm)

print(etapaUm)
print(etapaUmPontoUm)

print("\n---------------------------------\n")
print("parte 4\n")

# Fusão final:

# [27, 38, 43] e [3, 9, 10, 82] se tornam [3, 9, 10, 27, 38, 43, 82]
# A lista ordenada fica: [3, 9, 10, 27, 38, 43, 82].
final = etapaUm + etapaUmPontoUm
final = ordenar_lista(final)

print(final)
print("\n---------------------------------\n")

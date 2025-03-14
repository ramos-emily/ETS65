
#exercicio1
# num1 = int(input("digite um numero: "))
# num2 = int(input("digite um numero: "))

# result = num1 + num2
# print(f"a soma deles é {result}")


#exercicio2
# name = input("digite seu nome: ")
# year = int(input("digite em que ano nasceu: "))
# AnoAtual = 2025

# AtualIdade = (AnoAtual) - (year)

# print(f"em 2025 você terá {AtualIdade}")





#condicionais

#exercicio1
# num = int(input("digite um numero: "))

# if num%2 == 0:
#     print("seu numero é par!")
# else:
#     print("seu numero é impar!")


#exercicio2
# nota1 = int(input("digite a nota 1: "))
# nota2 = int(input("digite a nota 2: "))
# nota3 = int(input("digite a nota 3: "))
# nota4 = int(input("digite a nota 4: "))
# nota5 = int(input("digite a nota 5: "))

# media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# print(media)

# if media <2.5:
#     print("aluno REPROVADO!!")
# elif media >2.5 and media <5:
#     print("RECUPERAÇÃO!!")
# else:
#     print("aluno APROVADO!!")




#while/for

#exercicio1
# num = int(input("digite um numero inteiro positivo: "))

# for i in range(num+1):
#     print(i)

#exercicio2

# num = 0

# while (num >= 0):
#     num = int(input("digite um numero: "))
#     print("positivo")

# print("esse numero é negativo")




#funçao

#exercicio1
# s = ""

# def inverter_string(s):
#     palavra = input("digite uma palavra: ")
#     for i in palavra:
#         s = i + s
#     print(s)

# inverter_string(s)


#exercicio2


def contar_caracteres():
    palavra = input("digite uma palavra: ")
    lista = []
    for i, letra in enumerate(palavra):
       lista.append(f"{letra}{i+1}")

    print(" ".join(lista)) 
contar_caracteres()















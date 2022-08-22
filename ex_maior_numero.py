#Faça um Programa que peça dois números e imprima o maior deles.
num_1 = int(input("Digite um número de valor inteiro: "))
num_2 = int(input("Digite outro número de valor inteiro: "))

if num_1 > num_2:
    print(num_1)
elif num_1 < num_2:
    print(num_2)
else:
    print("Digite inteiros de valores diferentes")
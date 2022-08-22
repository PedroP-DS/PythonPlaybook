#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input("digite um número positivo ou negativo: "))

if valor >= 0:
    print(f"O número {valor} que você digitou é Positivo")
else:
    print(f"O número {valor} que você digitou é Negativo")
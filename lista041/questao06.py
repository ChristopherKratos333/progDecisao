'''
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print(f"O valor da subtração é {num1 - num2}")
else:
    print(f"O valor da subtração é {num2 - num1}")
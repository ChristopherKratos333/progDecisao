'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Digite um número inteiro negativo ou positivo: "))

if num > -1:
    print(f"O módulo deste número é {num}")
else:
    print(f"O módulo deste número é {num * -1}")
'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Informe um número: "))

if num > 0:
    print("Esse número é positivo.")
if num < 0:
    print("Esse número é negativo.")
if num == 0:
    print("Esse número é nulo.")
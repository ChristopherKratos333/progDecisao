'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = int(input("Informe um número: "))

if num % 2 == 0:
    print("O seu número é par.")
else:
    print("O seu número é ímpar.")
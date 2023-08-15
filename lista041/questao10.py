'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

resto = num1 % num2

if resto == 0:
    print("O segundo número informado é divisor do primeiro.")
else:
    print("O segundo número informado não é divisor do primeiro.")
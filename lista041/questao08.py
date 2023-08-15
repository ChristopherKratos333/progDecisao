'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Digite um número inteiro: "))

if num > 0 and num < 11:
    print(f"{num} está na faixa de 1 à 10!")
else:
    print(f"{num} não está na faixa de 1 à 10!")
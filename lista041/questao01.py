'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = float(input("Digite um número: "))

if (num > 20):
    print(f"A metade dele é: {num/2}")
else:
    print(f"O número é: {num}")
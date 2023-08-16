'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Informe um número: "))

mil = (f"{num} é menor que 1000.", f"{num} é maior ou igual a 1000.")[num>=1000]

print(mil)
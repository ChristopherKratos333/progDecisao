'''
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

a = int(input("Informe 3 números, Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a > b > c:
    maior = a

if a > c > b:
    maior = a

if b > a > c:
    maior = b

if b > c > a:
    maior = b

if c > a > b:
    maior = c

if c > b > a:
    maior = c

print(maior)
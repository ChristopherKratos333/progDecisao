'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Informe 3 valores, Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a < b < c:
    print(f"Em ordem crescente será: {a}, {b} e {c}")

if a < c < b:
    print(f"Em ordem crescente será: {a}, {c} e {b}")

if b < a < c:
    print(f"Em ordem crescente será: {b}, {a} e {c}")

if b < c < a:
    print(f"Em ordem crescente será: {b}, {c} e {a}")

if c < a < b:
    print(f"Em ordem crescente será: {c}, {a} e {b}")

if c < b < a:
    print(f"Em ordem crescente será: {c}, {b} e {a}")
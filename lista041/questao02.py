'''
Desenvolver um programa que permita ao aluno responder qual a capital do Brasil. O programa deverá exibir se
a resposta está certa ou errada.
'''

capital = input("Qual a capital do Brasil?\n")

if capital == 'Brasília':
    print(f"Sim! {capital} é a capital do Brasil!!")
else:
    print("A resposta está errada.")
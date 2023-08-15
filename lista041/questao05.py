'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

nota1 = float(input("Diga as 4 notas do aluno. Primeira: "))
nota2 = float(input("Segunda: "))
nota3 = float(input("Terceira: "))
nota4 = float(input("Quarta: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print(f"O aluno foi aprovado e sua média é {media}.")
else:
    print(f"O aluno não foi aprovado e sua média é {media}.")
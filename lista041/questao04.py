'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Informe um número: "))

if num % 4 == 0 and num % 5 == 0:
    print(f"O seu número divisível por 4 e 5 é: {num}")
else:
    print("Valor não é divisível por 4 e 5")
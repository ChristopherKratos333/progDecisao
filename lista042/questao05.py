'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigla = input("Escreva a sigla de um estado Brasileiro: ")

if sigla == 'ES' or sigla == 'SP' or sigla == 'RJ' or sigla == 'MG':
    print("O Estado inserido está localizado na região sudeste.")
else:
    print("O Estado inserido não está localizado na região sudeste.")
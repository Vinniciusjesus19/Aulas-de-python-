import os
os.system ('cls || clear')

#Iniciando variável 
resultado = False

#Solicitando dados ao susário.
a = int(input('Digite o primeiro número: '))
operador = input('Digite o operador: + - * /: ')
b = int(input('Digite o segundo número: '))

match(operador):
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*':
        resultado = a * b
    case '/':
        resultado = a / b
    case _:
        print('Operador inválido')


print(f'\nResultado: {resultado}')
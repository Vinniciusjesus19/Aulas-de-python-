import os

os.system("cls|| clear")

# Inicializando variavel.
resultado = False
while True:
    os.system("cls|| clear")

    #Solicitar dados do usuario.

    a = int(input('Digite o primeiro número: '))
    operador = input('Digite o operador: + - * /: ')
    b = int(input('Digite o segundo numero: '))
    match(operador):
        case '+':
            resultado = a + b
            break
        case '-':
            resultado = a - b
            break
        case '*':
            resultado = a * b
            break
        case '/':
            resultado = a / b
            break
        case _:
            input("Operador invalido")
if resultado :
        print(f"Resultado: {resultado}")

import os

os.system("cls|| clear")



# Inicializando variavel.
resultado = False
while True:
    os.system("cls|| clear")

    #Menu:
    print("\n===MENU===")
    print('Picanha: $25,00')
    print("Lasanha: $20,00")
    print("Strogronoff: $18,00")
    print("Bife Acebolado: $15,00")
    print("Pão com ovo: $5,00")
    print("\n")
    #Solicitar dados do usuario.

    operador = input('Digite de 1 a 5 para uma opção: ')
    
    match(operador):
        case '1':
            resultado = 'Picanha >> $25,00'
            break
        case '2':
            resultado = 'Lasnha >> $20,00'
            break
        case '3':
            resultado = 'Strogronoff >> $18,00'
            break
        case '4':
            resultado = 'Bife acebolado >> $15,00'
            break
        case '5':
            resultado = 'Pão com ovo >> $5,00'
            break

        case _:
            input("Menu invalido")
if resultado :
        print(f"Resultado: {resultado}")



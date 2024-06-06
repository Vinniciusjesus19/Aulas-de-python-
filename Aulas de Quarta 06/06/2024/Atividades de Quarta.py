import os

os.system("cls|| clear")

while True:
    os.system("cls|| clear")

    operador = input('Digite de 1 a 12 para um Mês do ano: ')
    
    match(operador):
        case '1':
            resultado = 'Janeiro'
            break
        case '2':
            resultado = 'Fervereiro'
            break
        case '3':
            resultado = 'Março'
            break
        case '4':
            resultado = 'Abril'
            break
        case '5':
            resultado = 'Maio'
            break
        case '6':
            resultado = 'Junho'
            break
        case '7':
            resultado = 'Julho'
            break
        case '8':
            resultado = 'Agosto'
            break
        case '9':
            resultado = 'Setembro'
            break
        case'10':
            resultado = 'Otubro'
            break
        case'11':
            resultado = 'Novembro'
            break
        case'12':
            resultado = 'Desembro'
            break
        
if resultado :
        print(f"Resultado: {resultado}")



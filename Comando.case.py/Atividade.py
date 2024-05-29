import os
os.system ('cls || clear')

#Iniciando variável 
resultado = False

while True:
    os.system ('cls || clear')
    #Solicitando dados ao susário.
    operador = int(input('Digite um dia da semana de 1 a 7: '))
    
    match(operador):
        case 1:
            resultado = 'Domingo'
            break
        case 2:
            resultado = 'Segunda-feira'
            break
        case 3:
            resultado = 'Terça-feira'
            break
        case 4:
            resultado = 'Quarta-feira'
            break
        case 5: 
            resultado = 'Quinta-feira'
            break
        case 6:
            resultado = 'Sexta-feira'
            break
        case 7:
            resultado = 'Sábado'
            break
        case _:
            input('Dia informado inválido')

if resultado:
    print(f'\nO dia selecionado foi: {resultado}')

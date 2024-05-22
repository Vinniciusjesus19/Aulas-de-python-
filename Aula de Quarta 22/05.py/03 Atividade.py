import os

os.system("cls || clear")

# Função para ler os números do usuário
def ler_numeros():
    numeros = []
    for i in range(6):
        numero = int(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
    return numeros

# Função para contar números pares e ímpares
def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Função principal
def main():
    # Ler os números
    numeros = ler_numeros()
    
    # Contar pares e ímpares
    pares, impares = contar_pares_impares(numeros)
    
    # Mostrar os números informados
    print("\nNúmeros informados:")
    for i, numero in enumerate(numeros, start=1):
        print(f"Número {i}: {numero}")
    
    # Mostrar a quantidade de pares e ímpares
    print(f"\nQuantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Executar a função principal
if __name__ == "__main__":
    main()
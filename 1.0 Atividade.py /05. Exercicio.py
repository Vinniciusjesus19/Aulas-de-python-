import os

os.system("cls|| clear")


# Inicializando contadores
pares = 0
impares = 0

# Lendo 5 valores inteiros
for i in range(5):
    valor = int(input("Digite o {}º valor inteiro: ".format(i + 1)))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrando o resultado
print("\nResultados:")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)


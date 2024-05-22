import os
os.system("cls || clear")

# Criando uma lista / vetor.
QUANTIDADES_NOTAS = 3

notas = []
soma = 0
media = 0

# Solicitando 3 notas para o usuário.
for i in range(QUANTIDADES_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
                 

for i in range(QUANTIDADES_NOTAS):
    print(f"nota: {notas [i]}")

media = soma + nota / 3

print(f"\n===RESULTADO===")
print(f"Nota informada: {nota}")
print(f"Média: {media}")

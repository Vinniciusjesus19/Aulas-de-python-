import os

os.system("cls|| clear")

print("\n===Solicitando dados ====")
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M ou F): ")
estadoCivil = input("Digite seu estado Civil: ")

if sexo == "F" and estadoCivil == "Casada":
    tempoDeCasamento = input("Digite o tempo de casada (em anos): ")

print("\n===Exibindo resultados ===")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estadoCivil}")
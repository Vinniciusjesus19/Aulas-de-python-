import os 

os.system ("cls || clear")

notas = []
while True:
    print("\nMenu:")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular a média aritmética das notas")
    opcao = input("Escolha uma opção: ").upper()

    if opcao == "S":
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    elif opcao == "P":
        print(f"Foram inseridas {len(notas)} notas.")
    elif opcao == "N":
        if len(notas) == 0:
            print("Não há notas inseridas.")
        else:
            media = sum(notas) / len(notas)
            print(f"A média aritmética das notas é: {media:.2f}")
    else:
        print("Opção inválida!")

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != "S":
        break


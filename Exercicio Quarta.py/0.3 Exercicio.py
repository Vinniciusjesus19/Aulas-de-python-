import os 

os.system ("cls || clear")

#solicitando Dados do usuario
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Nota inválida. A nota deve estar entre 0 e 10.")


print("A nota do aluno é:", nota)


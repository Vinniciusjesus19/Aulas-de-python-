import os 

os.system ("cls || clear")

#solicitando dados do usuario 
while True:
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
        break
    else:
        print("Nota inválida. As notas devem estar entre 0 e 10.")

media = (nota1 + nota2) / 2

print("A média do aluno é:", media)

import os 

os.system ("cls || clear")

# Solicita as notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 4:
    situacao = "Em recuperação"
else:
    situacao = "Reprovado"

print("A média das notas é:", media)
print("Situação do aluno:", situacao)

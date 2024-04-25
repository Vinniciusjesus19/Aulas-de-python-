import os  
os.system ("cls|| clear")

# Função para calcular a média e verificar se o aluno está aprovado ou reprovado
def calcular_media_e_status(nome, idade, primeiraNota, segundaNota, terceiraNota):
    media = (primeiraNota + segundaNota + terceiraNota) / 3
    if media < 7:
        status = "reprovado"
    else:
        status = "aprovado"
    return media, status

nome_aluno = input("Digite o nome do aluno: ")
idade_aluno = int(input("Digite a idade do aluno: "))
primeiraNota = float(input("Digite a primeira nota do aluno: "))
segundaNota = float(input("Digite a segunda nota do aluno: "))
terceiraNota = float(input("Digite a terceira nota do aluno: "))


media_aluno, status_aluno = calcular_media_e_status(nome_aluno, idade_aluno, primeiraNota, segundaNota, terceiraNota)

# Mostrando os resultados
print("\nDados do aluno:")
print("Nome:", nome_aluno)
print("Idade:", idade_aluno)
print("Média:", media_aluno)
print("Status:", status_aluno)
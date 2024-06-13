import os 
os.system ("cls || clear")

class Pet:
    def __init__(self, nome, idade, raca, porte, alimentacao):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    def __str__(self):
        return (f"Nome: {self.nome}\nIdade: {self.idade} anos\n"
                f"Raça: {self.raca}\nPorte: {self.porte}\n"
                f"Alimentação: {self.alimentacao}")

# Função para coletar dados do pet
def solicitar_dados_pet():
    nome = input("Digite o nome do pet: ")
    idade = int(input("Digite a idade do pet: "))
    raca = input("Digite a raça do pet: ")
    porte = input("Digite o porte do pet (pequeno, médio, grande): ")
    alimentacao = input("Digite a alimentação do pet: ")
    return Pet(nome, idade, raca, porte, alimentacao)

# Solicitando dados para dois pets
pet1 = solicitar_dados_pet()
pet2 = solicitar_dados_pet()

# Exibindo dados dos pets
print("\nDados do Pet 1:")
print(pet1)

print("\nDados do Pet 2:")
print(pet2)
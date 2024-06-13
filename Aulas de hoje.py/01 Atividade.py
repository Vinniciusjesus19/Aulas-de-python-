import os
from dataclasses import dataclass

os.system("cls || clear")

#constante.
QUANTIDADE_ALUNOS = 2

# classe.
@dataclass
class Aluno:
    nome: str
    idade: int
alunos = []

#Solicitando dados para o usúario.
for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome: ")
    idade__do_aluno = int(input("Digite sua idade: "))

    aluno = Aluno(nome = nome_do_aluno, idade = idade__do_aluno)
    alunos.append(aluno)

    #Exibindo dados para o usúario.
    for i in alunos:
        print(f"Nome: {i.nome}")
        print({f"Idade: {aluno.idade}"})                                                                                               
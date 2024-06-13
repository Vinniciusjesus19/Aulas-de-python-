import os 
os.system ("cls || clear")

class Livro:
    def __init__(self, titulo, autor, numero_paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.numero_paginas}\nPreço: R${self.preco:.2f}"

# Função para coletar dados do livro
def solicitar_dados_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    numero_paginas = int(input("Digite o número de páginas do livro: "))
    preco = float(input("Digite o preço do livro: "))
    return Livro(titulo, autor, numero_paginas, preco)

# Solicitando dados para dois livros
livro1 = solicitar_dados_livro()
livro2 = solicitar_dados_livro()

# Exibindo dados dos livros
print("\nDados do Livro 1:")
print(livro1)

print("\nDados do Livro 2:")
print(livro2)

import os

os. system ("cls || clear")

primeiroValor = (input("Digite o primeiro valor: "))
segundoValor = float (input("Digite o segundo valor: "))

soma = primeiroValor + segundoValor
media = soma /2
produto = primeiroValor * segundoValor

if primeiroValor > segundoValor:
    maiorNumero = primeiroValor 

else: menorValor = segundoValor

if primeiroValor < segundoValor:
    maiorNumero = segundoValor

    print ("\n===RESULTADO===")
    print (f"Primeiro valor: {primeiroValor}")
    print (f"Segundo valor: {segundoValor}")
    print (f"Soma: {soma}")
    print (f"media: {media}")
    print (f"Produto: {produto}")
    print (f"Maior numero: {maiorNumero}")
    print (f"Menor numero: {menorValor}")

 
import os  
os.system ("cls|| clear")

print ("=== solicitando dados === \n")
primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero 
subtaçao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero + segundoNumero
divisao = primeiroNumero / segundoNumero

print ("=== Exibindo resultados === \n")
print (f"Primeiro número: {primeiroNumero}")
print (f"Segundo número: {segundoNumero}")
print (f"Soma: {soma}")
print (f"Subtração: {subtaçao}")
print (f"Multiplicação: {multiplicacao}")
print  (f"Divisão: {divisao}")

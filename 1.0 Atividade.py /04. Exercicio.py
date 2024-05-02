import os

os.system ("cls || clear")

print ("\n==EXIBINDO DADOS==")

numero = int (input("Digite um numero entre 1 e 20: "))

for i in range (1, 20):
   if numero % 2 == 0:
      print ("numero e par: ")

   else:
      print ("esse numero e impar: ")

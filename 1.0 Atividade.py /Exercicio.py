import os 

os.sytem ("cls || clear")
import os

os.system("cls|| clear")

print("\n== Solicitando dados ===")
numero = int(input("Digite um numero para tabuada: "))

for i in range(1,11):
    print(f"numero {i}")

for i in range(10,0,-1):
    print(f"{numero} x {i} = {numero * i}")
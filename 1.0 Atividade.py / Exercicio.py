import os

os.system ("cls || clear")

#função para calcular o valor a ser pago pelo cliente 

print ("\n=== SOLICITANDO DADOS ===")
pesoMorangos = input ("Digite o peso do morangos (em kg): ")
pesoMacas = input ("Digite o peso de maçãs (em kg): ")

if pesoMorangos < 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20
 
if pesoMacas < 5:
       precoMaca = 1.80
else:
    precoMaca = 1.50

    pesoTotal = pesoMorangos + pesoMacas
    subTotal = (precoMorango * pesoMorangos) + (precoMaca * pesoMacas)

    if pesoTotal > 8 or subTotal > 25:
         desconto = subTotal * 0.10

    else: 
         desconto = 0

         totalPagar = subTotal - desconto

         print ("\n=== EXIBINDO RESULTADADOS ====")
         print (f"peso de morangos (em kg): {pesoMorangos} ")
         print (f"peso de maçãs (em kg): {pesoMacas}")
         print (f"soma dos pesos (em kg): {pesoTotal}")
         print (f"subtotal: R$ {subTotal}")
         print (f"desconto: R$ {subTotal: 2f}")
         print (f"total a pagar: R$ {totalPagar: 2f}")

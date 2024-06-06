# Solicita ao usuário o valor do produto
valor_produto = float(input("Informe o valor do produto: R$ "))

# Solicita ao usuário a forma de pagamento
print("Escolha a forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento à prazo")
forma_pagamento = int(input("Digite a opção (1 ou 2): "))

if forma_pagamento == 1:
    # Pagamento à vista
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print("\nForma de pagamento: à vista")
    print(f"Valor do produto: R$ {valor_produto:.2f}")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {valor_final:.2f}")
elif forma_pagamento == 2:
    # Pagamento à prazo
    parcelas = int(input("Digite a quantidade de parcelas: "))
    valor_parcela = valor_produto / parcelas
    print("\nForma de pagamento: a prazo")
    print(f"Valor do produto: R$ {valor_produto:.2f}")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcela: R$ {valor_parcela:.2f}")
    print(f"Total a prazo: R$ {valor_produto:.2f}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

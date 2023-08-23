# Crie um programa currency.py que pergunte ao usuário quanto ele tem em pesos, soles e reais e calcule o total em USD.

pesos = float(input("Digite a quantidade de pesos: "))
soles = float(input("Digite a quantidade de soles: "))
reais = float(input("Digite a quantidade de reais: "))

# Define as taxas de conversão atualizadas
taxa_peso_usd = 0.05
taxa_sole_usd = 0.25
taxa_real_usd = 0.20

# Calcula o total em dólares
total_usd = (pesos * taxa_peso_usd) + (soles * taxa_sole_usd) + (reais * taxa_real_usd)

print("O total em USD é:", total_usd)

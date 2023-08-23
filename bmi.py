# Crie um programa bmi.py que calcule seu próprio IMC.

def calcular_imc(peso, altura):
    altura_metros = altura / 100  # Converter altura de centímetros para metros
    imc = peso / (altura_metros ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em cm: "))

imc = calcular_imc(peso, altura)
interpretacao = interpretar_imc(imc)

print("Seu IMC é:", imc)
print("Interpretação:", interpretacao)

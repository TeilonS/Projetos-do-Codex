# Crie um programa hypotenuse.py que peça ao usuário dois números, ae b, e calcule a hipotenusa.

import math

# Solicita ao usuário os valores dos catetos a e b
a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

# Calcula a hipotenusa usando o teorema de Pitágoras
hipotenusa = math.sqrt(a**2 + b**2)

# Imprime o resultado
print("A hipotenusa é:", hipotenusa)


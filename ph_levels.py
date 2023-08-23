# Crie um programa ph_levels.py que verifica se um nível de pH é básico, ácido ou neutro.

grade = int(input('Digite a quantidade de ph (0-14): '))

if grade > 7:
  print('Basic')
elif grade < 7:
  print('Acidic')
elif grade == 7:
  print("Neutro")
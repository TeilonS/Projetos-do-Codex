# Pergunte ao usuário qual é a sua altura e quantos créditos ele tem, e armazene os valores em uma heightvariável e uma creditsvariável.

altura = int(input('Qual a sua altura(cm)? '))
créditos = int(input('Quantos créditos você tem? '))

if altura >= 137 and créditos >= 10:
  print("Aproveite o passeio! ")
if altura < 137 and créditos >= 10:
  print("Você não é alto o suficiente para montar. ")
if altura >= 137 and créditos < 10:
  print("Você não tem créditos suficientes. ")
if altura < 137 and créditos < 10:
  print("Você não é alto o suficiente e não possui créditos o suficiente.")
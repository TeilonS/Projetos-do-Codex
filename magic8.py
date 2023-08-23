# Crie um programa magic8.py que possa responder a qualquer pergunta Sim ou Não com uma resposta diferente cada vez que for executado.
import random


questão = input()

random_number = random.randint(1, 9)

if random_number == 1:
    print("Sim, definitivamente")
if random_number == 2:
    print("É decidamente assim")
if random_number == 3:
    print("Sem dúvidas")
if random_number == 4:
    print("Resposta nebulosa, tente novamente")
if random_number == 5:
    print("Pergunte novamente mais tarde")
if random_number == 6:
    print("Melhor não te dizer agora.")
if random_number == 7:
    print("Minhas fontes dizem não.")
if random_number == 8:
    print("As perspectivas não são tão boas.")
if random_number == 9:
    print("Muito duvidoso.")


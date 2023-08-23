# O Chapéu Seletor é um chapéu falante mágico da Escola de Magia e Bruxaria de Hogwarts.

# 🦁 Grifinória
# 🦅 Corvinal
# 🦡 Lufa-Lufa
# 🐍 Sonserina

grifinória_pontos = 1
corvinal_pontos = 1
lufa_lufa_pontos = 1
sonserina_pontos = 1

# Pergunta 1:

Questão1 = int(input(
    "Você prefere o Amanhecer ou o Crepúsculo?\n1) Amanhecer\n2) Crepúsculo\n"))

# Verificar a resposta da pergunta 1.

if Questão1 == 1:
    grifinória_pontos = 1
    corvinal_pontos = 1
elif Questão1 == 2:
    lufa_lufa_pontos = 1
    sonserina_pontos = 1
else:
    print("Entrada errada")

# Pergunta 2

Questão2 = int(input(
    "Quando eu morrer, quero que as pessoas se lembrem de mim como:\n1) O Bom\n2) O Grande\n3) O Sábio\n4) O Ousado\n"))

# Verifica a resposta da pergunta 2.

if Questão2 == 1:
    lufa_lufa_pontos += 2
elif Questão2 == 2:
    grifinória_pontos += 2
elif Questão2 == 3:
    corvinal_pontos += 2
elif Questão2 == 4:
    sonserina_pontos += 2
else:
    print("Entrada errada")

# Pergunta 3.

Questão3 = int(input(
    "Qual tipo de instrumento mais agrada seu ouvido?\n1) O violino\n2) A trombeta\n3) O piano\n4) O Tambor\n"))

# Verificar a resposta da pergunta 3.

if Questão3 == 1:
    sonserina_pontos += 4
elif Questão3 == 2:
    lufa_lufa_pontos += 4
elif Questão3 == 3:
    corvinal_pontos += 4
elif Questão3 == 4:
    grifinória_pontos += 4
else:
    print("Entrada errada")

# Imprima a casa com mais pontos.

if grifinória_pontos > corvinal_pontos and grifinória_pontos > lufa_lufa_pontos and grifinória_pontos > sonserina_pontos:
    print("Grifinória")
elif corvinal_pontos > grifinória_pontos and corvinal_pontos > lufa_lufa_pontos and corvinal_pontos > sonserina_pontos:
    print("Corvinal")
elif lufa_lufa_pontos > grifinória_pontos and lufa_lufa_pontos > corvinal_pontos and lufa_lufa_pontos > sonserina_pontos:
    print("Lufa-Lufa")
elif sonserina_pontos > grifinória_pontos and sonserina_pontos > corvinal_pontos and sonserina_pontos > lufa_lufa_pontos:
    print("Sonserina")
else:
    print("Empate")

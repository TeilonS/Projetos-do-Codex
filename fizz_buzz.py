# Crie um programa fizz_buzz.py que gere números de 1 a 100.
# Aqui está o problema:

# Para múltiplos de 3, imprima "Fizz" em vez do número.
# Para múltiplos de 5, imprima "Buzz" em vez do número.
# Aqui está a parte complicada: para múltiplos de 3 e 5, imprima "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

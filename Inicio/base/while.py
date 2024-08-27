import random

x = int(input("Digite un numero"))

soma = 0
for i in range(x):
    result = random.randint(1, 10)
    soma = soma + result
    print(result)
print(soma)
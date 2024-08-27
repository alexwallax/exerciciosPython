#leia 5 num e informe o maior

maior = 0

for i in range(5):
    num = int(input("Digite um numero: "))
    if num > maior:
        maior = num
print(f"O maior numero é {maior}")

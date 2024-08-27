nome = 0
senha = 0

while True:
    if nome == senha:
        nome = str(input("Digite seu nome "))
        senha = str(input("Digite sua senha "))
        print("Não pode repetir nome e senha")
    break
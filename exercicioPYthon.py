def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

def main():
    base = float(input("Insira o comprimento da base do triângulo: "))
    altura = float(input("Insira o comprimento da altura do triângulo: "))

    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print("A área do triângulo é:", area)
    else:
        print("Por favor, insira valores válidos maiores que zero para a base e altura.")

if __name__ == "__main__":
    main()
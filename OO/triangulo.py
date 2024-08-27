class Triangulo:
    ladoA = None
    ladoB = None
    ladoC = None
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def pegarMaiorLado(self):
        maiorLado = None
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            maiorLado = self.ladoA
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            maiorLado = self.ladoB
        elif self.ladoC > self.ladoA and self.ladoC > self.ladoB:
            maiorLado = self.ladoC
        else:
            maiorLado = "Todos os lados são iguais"
        return maiorLado
                
    
med1 = int(input("Informe o primeiro valor"))
med2 = int(input("Informe o segundo valor"))
med3 = int(input("Informe o terceiro valor"))

triangulo = Triangulo(med1, med2, med3)



print(triangulo.perimetro())
print(triangulo.pegarMaiorLado())



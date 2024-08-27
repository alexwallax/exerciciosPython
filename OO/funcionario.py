class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumento(self, aum):
        return self.salario * ((aum / 100) + 1)

harry = Funcionario("Harry", 1000)
print(harry.aumento(10))

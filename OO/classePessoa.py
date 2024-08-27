class Pessoa:
    nome = None
    idade = None

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self, anoAtual):
        return anoAtual - self.idade
    
pessoa = Pessoa("Pedro", 21)
print(pessoa.getAnoNascimento(2013))
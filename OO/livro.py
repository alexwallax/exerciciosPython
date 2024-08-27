class Livro:
    def __init__(self, nome, qtdPagina, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPagina
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        return self.preco
    
    def setPreco(self, valor):
        self.preco = valor
        return self.preco

valor1 = Livro("Maria", 50, "Jose", 100) 
print(valor1.getPreco())
valor1.setPreco(500)
print(valor1.preco)

        
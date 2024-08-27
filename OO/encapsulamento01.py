class Produto:
    qtdProd = 0

    def __init__(self, preco, codigo, qtdProd=0):
        self.__preco = preco
        self.__codigo = codigo
        self.qtdProd = qtdProd 
        Produto.qtdProd += 1

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco = preco 
        return self.__preco
    
    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self, codigo):
        self.__preco = codigo
        return self.__codigo


    def getList(self):
        for i in self.listProd:
            pass



class GerenciarProdutos:
    listProd = []

    def __init__(self):
        self.listaProd = []

    def adicionarProd(self, prod):
        self.listProd.append(prod)
        return self.listaProd
    
    def removeProd(self, cod_prod):
        for pro in self.listProd:
            if cod_prod == pro.getCod_prod():
                self.listProd.remove(pro)
                break
    

    def precoTotal(self, listacod):
        precoTotal = 0

        for j in listacod:

            for i in self.listProd:

                if cod_prod == i.getCod_prod():

                    precoTotal += self.listProd



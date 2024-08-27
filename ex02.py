
valorK = float(input("qual o valor do KWH: "))
potencia = float(input("Qual a potencia do chuveiro: "))
tempo = int(input("Tempo do banho: ")) / 60

preco = valorK * potencia * tempo

print("Valor do KWH ", valorK, " R$ ", "A Potência do chuveiro ", potencia )
print("Tempo de banho ", tempo * 60)
print("Total consumido com o tempo de banho ", preco)
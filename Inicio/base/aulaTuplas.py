#alterar o ultimo valor da tupla

tupla = (22, 55, 88)

#tranforma a tupla em lista
lista = list(tupla)

#troca o valor
lista[2]= 3

#transforma lista em tupla
lista = tuple(lista)

print(lista)
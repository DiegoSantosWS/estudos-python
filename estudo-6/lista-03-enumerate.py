print("Usando enumerate sem start/início")
estacoes = ["Primavera", "Verão", "Outono", "Inverno"]
lista_estacoes = list(enumerate(estacoes))
print(lista_estacoes)

print("\nUsando enumerate com start/início igual a 5")
lista_estacoes = list(enumerate(estacoes, start=5))
print(lista_estacoes)

print("Duas formas de mudar o número inicial de zero para 1")
itens = ["Carne Bovina", "Frango", "Salsicha", "Peixe", "Carne Suína"]

for indice, item in enumerate(itens, 1):
    print(indice, item)

print()
itens.sort()
for indice, item in enumerate(itens):
    print(indice+1, item)
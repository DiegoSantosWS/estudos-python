print("Criando um conjunto com valores informados.")
conjunto_numeros = {10, 30, 40, 10, 42, 42, 56}
print("conjunto_numeros: ", conjunto_numeros)

print("\nConvertendo uma lista em set.")
lista_frutas = ["Abacaxi", "Abacaxi", "Laranja", "Maçã", "Abacaxi"]
conjunto_frutas = set(lista_frutas)
print("conjunto_frutas: ", conjunto_frutas)

print("\nUnião.")
conjunto_uniao = conjunto_frutas.union(conjunto_numeros)
print("conjunto_uniao: ", conjunto_uniao)

print("\nDiferença.")
conjunto_diferenca = conjunto_uniao.difference(conjunto_numeros)
print("conjunto_diferenca: ", conjunto_diferenca) # Elementos de conjunto_uniao que não existem em conjunto_numeros

print("\nInterseção.")
conjunto_intersecao = conjunto_uniao.intersection(conjunto_numeros)
print("conjunto_intersecao: ", conjunto_intersecao) # Elementos comuns aos dois conjuntos

print("\nVerificando se um set inclui um outro set.")
if conjunto_uniao.issuperset(conjunto_numeros):
    print("conjunto_uniao inclui conjunto_numeros")

print("\nVerificando se um set inclui um outro set.")
conjunto_numeros_novo = {11, 21, 31, 41, 41, 41, 51}
if conjunto_uniao.issuperset(conjunto_numeros_novo):
    print("conjunto_uniao inclui conjunto_numeros_novo")
else:
    print("conjunto_uniao não inclui conjunto_numeros_novo")

print("\nVerificando se um set está incluso em outro set.")
if conjunto_numeros.issubset(conjunto_uniao):
    print("conjunto_numeros está em conjunto_uniao")

print("\nVerificando se um set possui elementos comuns a outro set.")
if conjunto_numeros_novo.isdisjoint(conjunto_numeros):
    print("conjunto_numeros_novo e conjunto_numeros não possuem elementos em comum")


print("Copiando e clonando listas")
lista_numeros = [1, 2, 3, 4, 5]
nova_lista = lista_numeros

print(lista_numeros)
print(nova_lista)

lista_numeros += [6]
print(lista_numeros)
print(nova_lista)

nova_lista += [7]
print(lista_numeros)
print(nova_lista)

lista_numeros = [1, 2, 3, 4, 5]
lista_clonada = lista_numeros[:]
lista_clonada += [6]
print(lista_numeros)
print(lista_clonada)
lista_numeros += [7]
print(lista_numeros)
print(lista_clonada)

print("\nFatiando listas")
linguagens = ["Python", "Cobol", "Clipper", "C", "C++", "Go", "JavaScript"]
linguagens2 = linguagens[3:5]
print(linguagens)
print(linguagens2)

print("\nFatiando listas")
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
letras[2:5] = ['C', 'D', 'E']
print(letras)
letras[2:5] = []
print(letras)
print("Lista original:")
bancos = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander"]
print(bancos)
print()

print("Incluindo um elemento (Bradesco) à lista com append:")
bancos.append("Bradesco")
print(bancos)
print()

print("Incluindo um elemento em uma posição específica com insert:")
bancos.insert(3, "Sicoob")
print(bancos)
print()

print("Removendo um elemento (CEF) da lista:")
bancos.remove("CEF")
print(bancos)
print()

print("Ordenando os itens da lista:")
bancos.sort()
print(bancos)
print()

print("Invertendo os itens da lista:")
bancos.reverse()
print(bancos)
print()

print("Retornando a quantidade de itens da lista com count.")
todos_bancos = ["Bradesco", "Banco do Brasil", "CEF", "Banestes", "Bradesco", "Bradesco"]
qtd_bradesco = todos_bancos.count("Bradesco")
print(f"Qtd. ocorrências Bradesco: {qtd_bradesco}")
numeros = [1, 10, 18, 45, 10, 7, 8, 9, 74, 10, 36, 10,  54, 65, 98, 10]
qtd_dez = numeros.count(10)
print(f"Qtd. Números dez: {qtd_dez}")
print()

print("Removendo o último elemento da lista:")
bancos.pop()
print(bancos)
print()

print("Removendo o último elemento da lista e armazenando em uma variável:")
banco = bancos.pop()
print(f"Banco: {bancos}")
print(f"Banco: {banco}")
print()

print("Removendo um elemento (Itaú) da lista com del:")
del bancos[1]
print(bancos)

print("Removendo elementos com del usando índice e fatia")
linguagens = ["Python", "Cobol", "Clipper", "C", "C++", "Go", "JavaScript"]
print(linguagens)
del linguagens[6] # Removeu JavaScript
print(linguagens)
del linguagens[1:3] # Removeu Cobol e Clipper
print(linguagens)

print("\nComparando duas listas")
lista1 = ["Cachorro", "Gato", "Galinha", "Papagaio"]
lista2 = ["Cachorro", "Gato", "Galinha", "Papagaio"]
lista3 = [1, 2, 3, 4, 5, 6, 7]

print("\nLimpando uma lista")
lista_livros = ['livro 1', 'livro 2', 'livro 3']
lista_livros.clear()
print(lista_livros)

lista_livros = ['livro 1', 'livro 2', 'livro 3']
lista_livros = []
print(lista_livros)
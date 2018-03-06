print("Tupla com parênteses")
linguagens = ("Assembly", "Cobol", "C", "C++")
print(linguagens)

# para saltar uma linha no resultado, deixando mais fácil sua leitura
# posso usar print() ou "\n" (quebra de linha)
print("\nTupla sem parênteses")
linguagens = "Python", "Java", "Go", "C#"
print(linguagens)

print("\nAcessando elementos pelo índice")
paises = "Brasil", "Paraguai", "Uruguai", "México"
pais = paises[0]
print(pais) # Brasil

print("\nFatiando tupla")
fatia = paises[1:3]
print(fatia) # ('Paraguai', 'Uruguai')

print()
print("Percorrendo elementos da tupla com for")
paises = "Brasil", "Paraguai", "Uruguai", "México"
for pais in paises:
    print(pais)

print("\nConvertendo uma lista em tupla usando tuple")
lista_carros = ["Gol", "Corolla", "Ranger", "Kadett", "Fusca", "Clio"]
tupla_carros = tuple(lista_carros)
print(f"Tupla carros: {tupla_carros}")

print("\nConvertendo uma tupla em lista usando list")
tupla_carros = "Gol", "Corolla", "Ranger", "Kadett", "Fusca", "Clio"
lista_carros = list(tupla_carros)
print(f"Lista carros: {lista_carros}")

print("\nDesempacotando elementos da tupla")
tupla_carros = "Golf", "Corolla", "Civic"
carro1, carro2, carro3 = tupla_carros
print(f"Carro1: {carro1}")
print(f"Carro2: {carro2}")
print(f"Carro3: {carro3}")

print("\nDesempacotando vários elementos para uma lista. Atribuição múltipla")
#Barra invertida indica que a linha continua
tupla_carros = "Golf", "Corolla", "Civic", "Opala", \
               "Tucson", "Elantra"
carro1, *carros = tupla_carros
print(f"Carro1: {carro1}")
print(f"Carros: {carros}") # Uma lista com os itens restantes

print("\nAtribuição múltipla não precisa estar no fim da sequência")
tupla_carros = "Golf", "Corolla", "Civic", "Opala", \
               "Tucson", "Elantra"
*carros, tucson, elantra = tupla_carros
print(f"Carros: {carros}")
print(f"Tucson: {tucson}")
print(f"Elantra: {elantra}")

print("\nUma lista como elemento de uma tupla")
tupla = ("Python", 10.25, 36, ["Ônibus", "Avião", "Navio", "Carro"])
print(tupla[0]) #Python
print(tupla[1]) # 10.25
print(tupla[2]) # 36
print(tupla[3]) # ['Ônibus', 'Avião', 'Navio', 'Carro']
lista = tupla[3]
print(lista) #['Ônibus', 'Avião', 'Navio', 'Carro'

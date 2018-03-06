# Usando o for com uma lista de números
numeros = [0, 18, 56, 77, 95]
for numero in numeros:
    print(f"Número: {numero}")
print("===================================================================================")
# Usando o for com uma lista de strings
frutas = ["Maçã", "Abacaxi","Melão", "Laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
print("===================================================================================")
# Usando o for com uma string
palavra = "Python"
for letra in palavra:
    print(letra)
print("===================================================================================")
# Usando else
numeros = [1, 2, 3, 10, 12]
for numero in numeros:
    print(f"Número:{numero}")
else:
    print("Acabou")
print("===================================================================================")
# Usando continue
for x in [1, 10, 20, 30, 40, 50]:
    if x == 30:
        continue
    print(x)
print("===================================================================================")
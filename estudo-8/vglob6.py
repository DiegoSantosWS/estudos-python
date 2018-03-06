TAXA_JUROS = 1.2 / 100

def calculo1(num1, num2):
    total = num1 + num2
    total += total * TAXA_JUROS
    print(f"Variáveis locais calculo1: {locals()}")
    print(f"Calculo1: {total}")

def calculo2(num1):
    total = 0
    for numero in num1:
        total += numero
    total += total * TAXA_JUROS
    print(f"Variáveis locais calculo2: {locals()}")
    print(f"Calculo2: {total}")

calculo1(25, 14)
numeros = [10, 50, 75.5, 96]
calculo2(numeros)
print(f"Variáveis globais: {globals()}")
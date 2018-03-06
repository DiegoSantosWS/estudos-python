TAXA_JUROS = 1.2 / 100

def calculo1(num1, num2):
    total = num1 + num2
    total += total * TAXA_JUROS
    print(f"Calculo1: {total}")

def calculo2(num1):
    total = 0
    for numero in num1:
        total += numero
    total += total * TAXA_JUROS
    print(f"Calculo2: {total}")

calculo1(10, 35)
valores = [10.0, 58.74, 65.41, 80.0]
calculo2(valores)
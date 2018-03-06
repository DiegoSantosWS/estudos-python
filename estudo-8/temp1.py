lista = [49, 42, True]

def somaTeste(val1, val2, imprime = False):
    resultado = val1 + val2
    if imprime:
        print(f"Soma: {resultado}")
    return resultado

total = somaTeste(*lista)

lista = [49, 42, True]

def somaTeste1(imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"SomaTeste1: {total}")
    return total

x = somaTeste1(False, 10,20,25,50,60,70)
print(x)
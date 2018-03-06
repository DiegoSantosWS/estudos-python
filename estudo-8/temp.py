def soma(val1, val2):
    return val1 + val2

total = soma(36, 47)
print(f"total: {total}")

def soma1(val1, val2, imprime = False):
    resultado = val1 + val2
    if imprime:
        print(f"Soma: {resultado}")
    return resultado

total = soma1(36, 50, True)

def soma2(val1, val2, imprime = False):
    print(f"valor1: {val1}")
    print(f"valor2: {val2}")
    resultado = val1 + val2
    if imprime:
        print(f"Soma: {resultado}")
    return resultado

total = soma2(val2=47, val1=150, imprime=True)

def multiplicar(v1, v2):
    return v1 * v2

def calcular(funcao, num1, num2):
    return funcao(num1, num2)

total = calcular(soma, 10, 25)
print(f"Soma: {total}")

total = calcular(multiplicar, 10, 25)
print(f"multiplicar: {total}")
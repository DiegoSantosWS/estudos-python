# Definindo uma função
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def divisao(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

# Fazendo uma chamada à função
valor = soma(10, 20)
print(f"Soma: {valor:.2f}")

valor = subtracao(75.2, 20)
print(f"Subtração: {valor:.2f}")

valor = multiplicacao(10, 20)
print(f"Multiplicação: {valor:.2f}")

valor = divisao(80, 3)
print(f"Divisão: {valor:.2f}")
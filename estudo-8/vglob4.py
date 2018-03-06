valor = 100.00

def calculo():
    global valor
    valor = 50.00
    print(f"Valor dentro da função: {valor}")

print(f"Valor fora da função: {valor}")
calculo()
print(f"Valor fora da função: {valor}")

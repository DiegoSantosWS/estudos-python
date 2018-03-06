salario_minimo = 937.00

def despesas_fixas():
    agua = 30.00
    luz = 100.00
    despesas = agua + luz
    saldo = salario_minimo - despesas
    print(f"Saldo despesas fixas: {saldo}")
    return despesas

def despesas_variaveis():
    supermercado = 500.00
    lanchonete = 100.00
    despesas = supermercado + lanchonete
    saldo = salario_minimo - despesas
    print(f"Saldo despesas variáves: {saldo}")
    return despesas

def despesas_mes():
    return despesas_fixas() + despesas_variaveis()

print(f"Salário mínimo: {salario_minimo}")
print(f"Despesas mês: {despesas_mes()}")
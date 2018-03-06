x = 0
soma = 0
quant_numeros = int(input("Quantos números deseja somar? "))
while x < quant_numeros:
    soma = soma + int(input("Informe um número inteiro para a soma: "))
    x = x + 1

print(f"Soma: {soma}")
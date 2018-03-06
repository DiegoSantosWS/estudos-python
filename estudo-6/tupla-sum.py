# Somando números informados pelo usuário usando uma tupla.
tupla_numeros = ()
while True:
    numero = int(input("Informe um número inteiro (zero para sair): "))

    if numero == 0:
        break
    tupla_numeros += (numero, )

soma = 0
for numero in tupla_numeros:
    soma += numero

print(f"A soma dos números é: {soma}")
#Somando números do intervalo informado limitando o maior número
inicio = int(input("Informe o primeiro número: "))
fim = int(input("Informe o número final: "))
salto = int(input("Informe o salto: "))
texto = "Cálculo: "
soma = 0
for numero in range(inicio, fim, salto):
    soma = soma + numero
    texto = texto + str(numero)
    if numero > 50:
        texto = texto + " Passou de 50"
        break
    if numero != fim-1:
        texto = texto + " + "
print(texto)
print(f"Soma: {soma}")
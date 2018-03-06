# Uma função recebendo um parâmetro denominado valores
# Errata: Na aula eu disse que a função maior valor tinha
# como parâmetro uma lista de valores me referindo ao
# fato de que eu vou fornecer uma lista que é a lista_numeros
# porém, o parâmetro "valores" não tem um tipo de dados definido
# eu poderia passar uma string ou um inteiro por exemplo
# o problema é que se eu fornecer um inteiro, vai dar erro
# na função max.
# Só pra deixar claro que "valores" não é definido como
# um parâmetro do tipo lista

def maior_valor(valores):
    return max(valores)

def capturar_numeros():
    lista_numeros = []
    while True:
        numero = int(input("Informe um número inteiro ou zero para sair: "))
        if numero == 0:
            break
        lista_numeros.append(numero)
    return maior_valor(lista_numeros)

# Chamada da função
print(f"Maior valor: {capturar_numeros()}")
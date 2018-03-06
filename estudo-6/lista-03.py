print("Lista com listas")
lista = [10.2, 13.75, 17.58, ["Maçã", "Banana", "Abacaxi"]]
print(lista)
frutas = lista[3]
print(frutas)
soma = lista[0] + lista[1] + lista[2]
print(soma)

print()
print("Lista com listas 2")
letras = ['a', 'b', 'c', 'd']
numeros = [1, 2, 3]
mistura = [letras, numeros]
print(mistura)
print(mistura[0])
print(mistura[1])

print()
print("Obtendo o tamanho de uma lista:")
lista = [100, 752, 845, 15, 74]
tamanho = len(lista)
print(tamanho)

print()
print("Obtendo o índice de um determinado elemento:")
linguagens = ["Java", "Python", "Go", "Pascal", "C#"]
print(linguagens.index("Python"))

print()
print("Verificando a existência de um item na lista:")
linguagens = ["JAVA", "PYTHON", "GO", "PASCAL", "C", "JAVASCRIPT"]
linguagem = input("Informe a linguagem: ")
if linguagem.upper() in linguagens:
    print(f"{linguagem.upper()} está na lista.")
else:
    print(f"{linguagem.upper()} não está na lista.")

print()
print("Adicionando elementos fornecidos pelo usuário à lista")
lista = []
while True:
    numero = int(input("Digite um número inteiro (informe 0 para sair): "))
    if numero == 0:
        break
    lista.append(numero)
x = 0
for num in lista:
    print(num)
lista = []
conjunto = set()
while True:
    entrada_usuario = input("Informe um número ou 'sair' para finalizar: ")
    if entrada_usuario == "sair":
        break
    lista.clear()
    lista.append(entrada_usuario)

    if conjunto.issuperset(set(lista)):
        print(f"O número {entrada_usuario} já foi informado!")
    else:
        conjunto = conjunto.union(set(lista))
        print("O número informado foi inserido.")

print("Conjunto:", conjunto)

def funcao_externa():
    a = 20
    b = 80
    print(f"Imprimindo 'b' em função externa: {b}")
    print(f"Imprimindo 'a' em função externa: {a}")
    def funcao_interna():
        c = 30
        b = 25
        global a
        a = 70
        print(f"Imprimindo 'c' em função interna: {c}")
        print(f"Imprimindo 'b' em função interna: {b}")
        print(f"Imprimindo 'a' em função interna: {a}")
    funcao_interna()
    print(f"Imprimindo 'b' de novo em função externa: {a}")

a = 20
print(f"Imprimindo 'a' no escopo global: {a}")
funcao_externa()
print(f"Imprimindo 'a' de novo no escopo global: {a}")
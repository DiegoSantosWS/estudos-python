tabuada = [
    lambda x: f"{x} * 1 = " + str(x * 1),
    lambda x: f"{x} * 2 = " + str(x * 2),
    lambda x: f"{x} * 3 = " + str(x * 3),
    lambda x: f"{x} * 4 = " + str(x * 4),
    lambda x: f"{x} * 5 = " + str(x * 5),
    lambda x: f"{x} * 6 = " + str(x * 6),
    lambda x: f"{x} * 7 = " + str(x * 7),
    lambda x: f"{x} * 8 = " + str(x * 8),
    lambda x: f"{x} * 9 = " + str(x * 9),
    lambda x: f"{x} * 10 = " + str(x * 10)
]

numero = int(input("Informe o numero para gerar a tabuada: "))
for x in tabuada:
    print(x(numero))
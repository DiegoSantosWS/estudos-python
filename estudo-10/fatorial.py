def fatorial(x):
    if x <= 1:
        return 1
    else:
        return (x * fatorial(x -1))
n = int(input("Informe um numero para encontar o fatorial: "))

print("O fatorial de:", n, "é", fatorial(n))

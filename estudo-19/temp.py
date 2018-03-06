valor = input("Informe um numero: ")
try:
    soma = int(valor) + 10
    resultado = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro na divisao")
except ValueError:
    print("Ocorreu um erro de str")
else:
    print("Não deu nenhum erro")
finally:
    print("Sempre será executado")

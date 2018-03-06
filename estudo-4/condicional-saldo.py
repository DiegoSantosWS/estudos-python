limiteCredito = 900
totalCompras = 325.56
saldoDisponivel = limiteCredito - totalCompras

valorCompra = float(input("Informe o valor da compra: "))
if valorCompra <= saldoDisponivel:
    saldoDisponivel = saldoDisponivel - valorCompra
    print("Sua compras foi autorizada.\n"
          f"Valor da compra: R$ {valorCompra:.2f}\n"
          f"Seu saldo atualizado é: {saldoDisponivel:.2f}")
else:
    print("Sua compras não foi autorizada.\n"
          f"Saldo insuficiente.\n"
          f"Saldo disponivel é: {saldoDisponivel:.2f}")
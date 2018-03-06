# Dicionário com lista
# "estoque": código, [nome_produto, qtd_estoque, valor]
estoque = { "1": ["Teclado", 300, 166.71],
            "2": ["Mouse", 125, 80.57],
            "3": ["Processador", 25, 875.64],
            "4": ["Cooler", 70, 35.14]}

produtos_comprados = {}
total_geral = 0
while True:
    codigo_produto = input("Informe o código ou zero (0) para sair: ")
    if codigo_produto == "0":
        break
    if codigo_produto in estoque:
        qtd = int(input("Informe a quantidade: "))
        confirma = input("Confirma? 'S' para sim ou 'N' para não: ")
        if confirma == 'S':
            total_produto = 0
            estoque[codigo_produto][1] -= qtd
            valor_unitario = estoque[codigo_produto][2]
            total_produto = valor_unitario * qtd
            total_geral += total_produto
            produtos_comprados[codigo_produto] = (codigo_produto,
                                                  estoque[codigo_produto][0],
                                                  qtd,
                                                  f"R$ {valor_unitario:.2f}",
                                                  f"R$ {total_produto:.2f}")
        else:
            print("Você desistiu do produto.")
    else:
        print("Produto não encontrado no estoque.")

print(f"Estoque: {estoque}")
print(f"Produtos comprados: {produtos_comprados}")





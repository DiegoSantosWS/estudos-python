notas = 0
quant_notas_informadas = 0

while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if nota == -1:
        break
    notas = notas + nota
    quant_notas_informadas = quant_notas_informadas + 1

if quant_notas_informadas > 0:
    media = notas / quant_notas_informadas
    print(f"Quantidade de notas informadas: {quant_notas_informadas}")
    print(f"Média: {media}")
else:
    print("Nenhuma nota informada.")

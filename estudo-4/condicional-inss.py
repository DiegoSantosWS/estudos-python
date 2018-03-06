salario_informado = float(input("Informe o salario: "))
salario_contribuicao = salario_informado
if (salario_contribuicao <= 1659.38):
    alicota_inss = 8
elif (salario_contribuicao <= 2765.66):
    alicota_inss = 9
elif (salario_contribuicao <= 5531.31):
    alicota_inss = 11
else:
    salario_contribuicao = 5531.31
    alicota_inss = 11
valor_inss = (salario_contribuicao * (alicota_inss/100))
salario_liquido = salario_informado - valor_inss

print(f"O salário contribuição é: {salario_contribuicao:.2f}.\n"
      f"A alicota de INSS é de: {alicota_inss:.1f}%.\n"
      f"Será descontado R$ {valor_inss:.2f}. de INSS\n"
      f"Descontado o INSS você receberá R$ {salario_liquido:.2f}.")
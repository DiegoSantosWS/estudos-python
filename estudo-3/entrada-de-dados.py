nome_completo = input("Informe a resposta correta:\n "
"Qual linguagem vc está aprendendo agora?\n"
"a) Python\n"
"b) PHP\n"
"resposta: ")
print("sua resposta foi: ", nome_completo)

valor_fixo = 45
resposta = int(input("Informe um número de 1 a 10: "))
soma = valor_fixo + resposta
print(soma)

print("===============================================================")

valor_fixo = 45.5
resposta = float(input("Informe um número de 1 a 10: "))
soma = valor_fixo + resposta
print(soma)
print("===============================================================")

valorUnitario = float(input("Informe o valor do produto: "))
quantidade = int(input("Informe a qtd de produtos: "))
print(f"O total da compra é: {valorUnitario * quantidade}")
'''
tamanho_name = len(nome_completo)
if (tamanho_name >=6):
    print(f"Seu nome é: {nome_completo}")
else:
    print("informe seu nome por favor!:")
'''
# Criando o dicionário
carros = {'marca': 'VW', 'modelo': 'Gol', 'ano_modelo': 2017}

# Acessando seus elementos
print(f'O ano do modelo do carro é: {carros["ano_modelo"]}')
print(f"A marca do carro é: {carros['marca']}")

# Adicionando elementos ao dicionário
carros['ano_fabricacao'] = 2018
print(f'O ano do fabricação do carro é: {carros["ano_fabricacao"]}')

# Apagando um elemento
del carros['modelo']
print(f"Removido modelo: {carros}")

carros['modelo'] = "Golf"
print(f"Adicionado modelo: {carros}")

# Obtendo itens, chaves e valores
print(f'Itens do dicionário carros: {carros.items()}')
print(f'Chaves do dicionário carros: {carros.keys()}')
print(f'Valores do dicionário carros: {carros.values()}')

# keys(), items() e values() retornam "Views", que são iteradores
# dos tipos dict_keys, dict_items e dict_values que devolvem
# um elemento de cada vez.

# Verificando se uma chave existe no dicionário
if "Quilometragem" in carros:
    print("Quilometragem informada")
else:
    print("Quilometragem não informada")

print("Removendo todos elementos com clear")
print(f"Carros: {carros}")
carros.clear()
print(f"Carros: {carros}")

print("Copiando um dicionário para outro")
dic1 = {'nome': 'Fulano', 'sobrenome': 'de Tal'}
dic2 = dic1.copy()
print(f'dic1: {dic1}')
print(f'dic2: {dic2}')

print("Adicionado um dicionário em outro dicionário")
dic1 = {'nome': 'Fulano', 'sobrenome': 'de Tal'}
dic2 = {'idade': 40, 'UF': 'ES'}
print(f'dic1: {dic1}')
print(f'dic2: {dic2}')
dic1.update(dic2)
print(f'dic1: {dic1}')

print("Retornado o tamanho do dicionário.")
print(f'len(dic1): {len(dic1)}')
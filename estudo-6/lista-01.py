# Criando uma lista com 3 inteiros
lista_numeros = [25, 78, 55]

#  Os elemetos da lista iniciam com zero
#  0=25, 1=78, 2=55
#  Na linha abaixo será impresso 78
print(lista_numeros[1])

#  Alterando o segundo elemento da lista de 78 para 30
lista_numeros[1] = 30
# Na linha abaixo será impresso 30
print(lista_numeros[1])

# Acessando os elementos para calcular a média
notas = [7.5, 5.6, 9.5, 10.0]
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print(media)

# Alterando itens da lista pelo seu índice, outro exemplo:
bancos = ["Banco do Brasil", "CEF", "Banestes"]
print(bancos) # Resultado: ['Banco do Brasil', 'CEF', 'Banestes’]

bancos[1] = "Itaú"
print(bancos) # Resultado: ['Banco do Brasil', 'Itaú', 'Banestes’]

#Assim como no fatiamento de string, o último elemento de uma lista pode ser acessado pelo índice -1.
bancos = ["Banco do Brasil", "CEF", "Banestes"]
bancos[-1] = "Itaú"
print(bancos) # Resultado: ['Banco do Brasil', 'CEF', ’Itaú’]

#Para incrementar o valor de uma lista podemos usar o operador de adição.
numeros = [1, 2, 3, 10, 12]
numeros = numeros + [8, 7, 15]
print(numeros) #Resultado:[1, 2, 3, 10, 12, 8, 7, 15]

# Mas também podemos fazer assim, usando o operador de atribuição com adição “+=”:
numeros = [1, 2, 3, 10, 12]
numeros += [8, 7, 15]
print(numeros) # Resultado [1, 2, 3, 10, 12, 8, 7, 15]

bancos = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Sicoob", "Bradesco"]
bancos += ["Real", "Safra", "Santander"]
# Resultado: ['Banco do Brasil', 'CEF', 'Banestes', 'Itaú’,
#             'Sicoob', 'Bradesco', 'Real', 'Safra', 'Santander']
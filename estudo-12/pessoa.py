class Pessoa():

    especie = "Humano"

print(Pessoa.especie)
Pessoa.vivo = True
print(Pessoa.vivo)


homem = Pessoa()
print(homem.especie)
print(homem.vivo)

Pessoa.vivo = False
print(Pessoa.vivo)


homem = Pessoa()
homem.nome = "Diego "
homem.sobrenome = "Santos"
print(homem.nome, homem.sobrenome)


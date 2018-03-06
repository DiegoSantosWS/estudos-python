from pessoa_fisica import Pessoa_fisica
from pessoa_juridica import Pessoa_juridica

pf = Pessoa_fisica("016.688.066-30", "Diego Santos", 30)
pj = Pessoa_juridica("00.000.000/0001-12", "Loja teste", 60)

print(pf.nome)
print(pf.idade)
print(pf.cpf)

print(pj.nome)
print(pj.idade)
print(pj.cnpj)
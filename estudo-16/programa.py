from pessoa import Pessoa

p = Pessoa("José")
#print(p.nome)

def pegar_nome(self):
    return self.nome

Pessoa.pegar_nome = pegar_nome
#print(p.pegar_nome())

def mudar_nome(self, novo_nome):
    self.nome = novo_nome

Pessoa.mudar_nome = mudar_nome
p.mudar_nome("Diego Santos")
#print(p.pegar_nome())

Pessoa.sobre_nome = "Batista"

def imprimir_ola(self):
    print("Olá", self.nome, self.sobre_nome)
Pessoa.ola = imprimir_ola
p.ola()
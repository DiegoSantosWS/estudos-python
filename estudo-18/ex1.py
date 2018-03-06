class MeuDescritor(object):
    def __init__(self, valInicial=None, nome="my_var"):
        self.valor = valInicial
        self.nome = nome
    
    def __get__(self, instance, owner):
        print("Obtendo:", self.nome)
        return self.valor
    
    def __set__(self, instance, valor):
        print(f"Atribuindo {valor} a {self.nome}")
        self.valor = valor

class MinhaClasse(object):
    
    descritor = MeuDescritor(valInicial='10', nome='dinheiro')
    normal = 20

classe = MinhaClasse()
print(classe.descritor)
print(classe.normal)
classe.descritor = 200
print(classe.descritor)
classe.normal = 150
print(classe.normal)
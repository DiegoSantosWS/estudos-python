'''
DESCRITORES
'''

class RevelarAcesso(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
    
    def __get__(self, instance, owner):
        print("Recuperando", self.name)
        return self.val
    
    def __set__(self, instace, value):
        print("Atualizando", self.name)
        self.val = value

class MinhaClasse(object):
    x = RevelarAcesso(10,  'var "x"')
    y = 5


m = MinhaClasse()
print("x:", m.x)
m.x = 20
print("x:", m.x)
print()
print("y:", m.y)
m.y = 8
print("y:", m.y)
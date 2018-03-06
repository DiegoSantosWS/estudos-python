import sys

class Exemplo(object):
    def __init__(self):
        self.contador = 0
        print("Limite recursividade: ", sys.getrecursionlimit())
        sys.setrecursionlimit(10)
        print("Limite recursividade: ", sys.getrecursionlimit())
    def funcao_recursiva(self):
        self.contador += 1
        print("Contador: ", self.contador)
        if self.contador < sys.getrecursionlimit():
            self.funcao_recursiva()

ex = Exemplo()
ex.funcao_recursiva()
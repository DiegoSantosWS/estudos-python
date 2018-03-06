class Classe_base():

    def __init__(self, val1, val2):
        print("Metodo construtor da classe")
        self.val1 = val1
        self.val2 = val2
    
    def somar(self):
        return self.val1 + self.val2
    
    def subtrair(self):
        return self.val1 - self.val2
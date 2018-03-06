from aquatico import Aquatico
class Barco(Aquatico):
    def __init__(self, velocidadeNaAgua, qtdHelices):
        self.qtdHelices = qtdHelices
        super().__init__(velocidadeNaAgua)

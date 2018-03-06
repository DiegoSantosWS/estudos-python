from carro import Carro
from barco import Barco

class Anfibio(Carro, Barco):
    def __init__(self, velocidadeEmTerra, velocidadeNaAgua, qtdPortas, qtdHelices):
        self.velocidadeEmTerra = velocidadeEmTerra
        self.velocidadeNaAgua  = velocidadeNaAgua
        self.qtdPortas         = qtdPortas
        self.qtdHelices        = qtdHelices

        #Carro.__init__(self, velocidadeEmTerra, qtdPortas)
        #Barco.__init__(self, velocidadeNaAgua, qtdHelices)
        super().__init__(velocidadeEmTerra=velocidadeEmTerra,
                         velocidadeNaAgua=velocidadeNaAgua,
                         qtdPortas = qtdPortas, qtdHelices = qtdHelices)

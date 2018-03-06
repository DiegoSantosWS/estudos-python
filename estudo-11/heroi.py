class Heroi:
    """
    Essa nossa classe de herois
    """

    def __init__(self, voa, lancaTeia, possueArma, fraseComum):    
        self.voa = voa
        self.lancaTeia = lancaTeia
        self.possueArma = possueArma
        self.fraseComum = fraseComum

    def falar(self):
        print(self.fraseComum)
    
    def detalhar(self):
        if self.voa:
            print("O heroi via")
        if self.lancaTeia:
            print("O heroi lança teia")
        if self.possueArma:
            print("O heroi possúe arma")
class Veiculo():
    
    def __init__(self, possui_motor, qtd_rodas):
        self.possui_motor = possui_motor
        self.qtd_rodas = qtd_rodas
        self.ligado = False

    def ligar(self):
        if self.possui_motor:
            self.ligado = True
            print("Ligou:")
        else:
            print("Não tem motor")
    
    def desligar(self):
        if self.possui_motor:
            if self.ligado:
                print("Desligou")
            else:
                print("Não esta ligado")
        else:
            print("não tem motor")
    
    def andar(self):
        print("O veiculo começou a andar")
    
    def parar(self):
        print("O veiculo parou")
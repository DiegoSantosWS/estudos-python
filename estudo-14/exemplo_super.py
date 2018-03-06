class Pai():
    def __init__(self):
        print("Construtor da classe pai")

class Mae():
    def __init__(self):
        print("Construtor da classe mae")

class Filha(Pai):
    def __init__(self):
        super().__init__()

filha = Filha()

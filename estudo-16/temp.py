class Cachorro():
    def som(self):
        print("Au au")

class Gato():
    def som(self):
        print("Miau")


def emitirSom(a):
    a.som()


dog = Cachorro()
cat = Gato()

emitirSom(dog)
emitirSom(cat)
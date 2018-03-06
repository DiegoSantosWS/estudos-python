class Quadrado():
    lados = 8

    def area(self):
        return self.lados ** 2

quadrado = Quadrado()
print(quadrado.area())

print(Quadrado.area(quadrado))

quadrado.lados = 10
print(quadrado.area())

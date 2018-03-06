class Calculo():
    
    def calcular_total(self, quantidade, desconto):
        return (self.preco * quantidade - desconto)

calc = Calculo()
calc.preco = 15

print(calc.calcular_total(15, 10))

print(Calculo.calcular_total(calc, 15, 10))
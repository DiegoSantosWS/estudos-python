from classe_derivada1 import Classe_derivada1
from classe_derivada2 import Classe_derivada2

class Classe_teste():
    
    calculo = Classe_derivada1(10, 20)
    resultado = calculo.somar()
    print(resultado)
    resultado = calculo.subtrair()
    print(resultado)
    calculo.imprimir("Olá mundo!")

    calc = Classe_derivada2(14, 85)
    resuldado = calc.multiplicar(20, 14)
    print(resuldado)

    resulta = calc.somar()
    print(resulta)



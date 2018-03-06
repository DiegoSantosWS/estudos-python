class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros_percorridos = metros
        self._tempo_gasto = segundos
        self._velocidade = self._metros_percorridos / self._tempo_gasto
    
    @property
    def velocidade(self):
        print("Executou get_velocidade")
        return f"a média de velocidade foi: {self._velocidade:.2f} metros por segundo"

    @velocidade.setter
    def velocidade(self, velocidade):
        print("Executou set_velocidade")
        self._velocidade = velocidade

    @velocidade.deleter
    def velocidade(self):
        print("Executou del_velocidade")
        del self._velocidade

    
a = Arrancada(10, 30)
print(a.velocidade)
a.velocidade = 35
print(a.velocidade)
del a.velocidade
from carta import *
from random import shuffle

class Mazo:
    def __init__(self, jugador = False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [Carta(v, p) for v in [str(x) for x in range(2,11)] + ['A', 'J', 'Q', 'K'] 
                           for p in self.pintas] 
            shuffle(self.cartas)

    def mostrar_cartas(self):
        for c in self.cartas:
            print(c.mostrar_carta())

    def obtener_valor_mazo(self):
        valor = 0
        con_as = False
        for c in self.cartas:
            valor += c.obtener_valor()
            if c.valor == 'A':
                con_as = True
        if con_as and valor <= 11:
            valor += 10
        return valor
    
    def entregar_carta(self):
        self.cartas[0].obtener_ruta()
        return self.cartas.pop(0)

class MazoFrances(Mazo):
    def __init__(self, jugador=False):
        self.pintas = ['Diamantes', 'Corazones', 'Picas', 'Trebol']
        super().__init__(jugador)


class MazoEspanol(Mazo):
    def __init__(self, jugador=False):
        self.pintas = ['Bastos', 'Espadas', 'Monedas', 'Copas']
        super().__init__(jugador)


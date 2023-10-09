from carta import *
from random import shuffle
class Mazo: 
    def __init__(self, jugador = False) -> None:
        if jugador:
            self.cartas=[]
        else:
            self.cartas =[ Carta(v,p) for v in [str(x) for x in range(2,11)] +['A','J','K','Q'] for p in ['Diamantes',"Corazones","Picas","Treboles"] ]
            shuffle(self.cartas)

    def mostrar_cartas(self):
        for c in self.cartas:
            print(c.mostrar_carta())
    
    def obtener_valor_maso(self):
        valor = 0 
        con_as = False
        for c in self.cartas:
            valor += c.obtener_valor()
            if c.valor == "A":
                con_as = True
        if con_as and valor < 11:
            valor += 10
        return valor
    
    def entregar_carta(self):
        return self.cartas.pop(0)

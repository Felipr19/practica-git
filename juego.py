from mazo import *

class juego:

    def __init__(self, mazo):
        self.mazo = mazo
        self.jugador1 = Mazo(True)
        self.jugador2 = Mazo(True)

    def iniciar_juego(self):
        for _ in range(2):
            self.jugador1.cartas.append(self.mazo.entregar_carta())
            self.jugador2.cartas.append(self.mazo.entregar_carta())
    
    def mostrar_juego(self):
        print("Casa:")

    def valorar_juego(self):
        valor_casa = self.jugador1.obtener_valor_maso()
        valor_jugador = self.jugador2.obtener_valor_maso()

        if valor_jugador > valor_casa and valor_jugador <= 21:
            print("jugador gana")
        elif valor_jugador <= 21 and valor_casa >21:
            pritn("jugador gana")
        elif valor_casa <= 21:
            print("Casa gana")

    def jugar(self):
        while self.jugador2.obtener_valor_maso() < 18:
            self.jugador2.cartas.append(self.mazo.entregar_carta())
            self.mostrar_juego()
        while self.jugador1.obtener_valor_maso() < self.jugador2.obtener_valor_maso() and self.jugador1.obtener_valor_maso() < 21:
            self.jugador1.cartas.append(self.aza.entregar_carta())
            self.mostrar_juego()

    
from mazo import *

class Juego:
    def __init__(self, mazo):
        self.mazo = mazo
        self.Casa = Mazo(True)
        self.Jugador = Mazo(True)

    def iniciar_juego(self):
        for i in range(2):
            self.Casa.cartas.append(self.mazo.entregar_carta())
            self.Jugador.cartas.append(self.mazo.entregar_carta())

    def mostrar_juego(self):
        print("Casa:")
        self.Casa.mostrar_cartas()
        print("Valor mano: ", self.Casa.obtener_valor_mazo())

        print("Jugador:")
        self.Jugador.mostrar_cartas()
        print("Valor mano: ", self.Jugador.obtener_valor_mazo())
       

    def valorar_juego(self):
        valor_casa = self.Casa.obtener_valor_mazo()
        valor_jugador = self.Jugador.obtener_valor_mazo()

        if valor_jugador > valor_casa and valor_jugador <= 21:
            print("Jugador gana")
            return True
        elif valor_jugador <= 21 and valor_casa > 21:
            print("Jugador gana")
            return True
        elif valor_casa <= 21:
            print("Casa gana")
            return False

    def jugar(self):
        while self.Jugador.obtener_valor_mazo() < 18:
            self.Jugador.cartas.append(self.mazo.entregar_carta())
            self.mostrar_juego()
        while self.Casa.obtener_valor_mazo() < self.Jugador.obtener_valor_mazo() and self.Casa.obtener_valor_mazo() < 21 and self.Jugador.obtener_valor_mazo() <= 21:
            self.Casa.cartas.append(self.mazo.entregar_carta())
            self.mostrar_juego()



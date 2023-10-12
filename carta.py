import pygame

class Carta:
    def __init__(self, valor, pinta):
        self.pinta = pinta
        self.valor = valor
        self.imagen = None


    def obtener_valor(self):
        if self.valor == 'A':
            return 1
        if self.valor in ['J', 'Q', 'K']:
            return 10
        return int(self.valor)

    def obtener_ruta(self):
        if self.pinta in ['Bastos', 'Espadas', 'Monedas', 'Copas']:
    
            if self.valor in ('J','K','Q'):
                valor = 10
            elif self.valor == 'A':
                valor = 1
            else:
                valor = self.valor
            
            ruta=f"Baraja_Espanola\{self.pinta}\{self.pinta}_{valor}.jpg" 

        else:
            ruta=f"Baraja_Francesa\{self.pinta}\{self.pinta}_{self.valor}.png" 

        
        self.imagen =pygame.image.load(ruta)

    def mostrar_carta(self):
        return self.pinta, self.valor
    



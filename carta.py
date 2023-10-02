class Carta:    
    def __init__(self):
        self.pinta = None
        self.valor = None

    def obtener_valor(self):
        if self.valor == "A":
            return 1 
        if self.valor in ['j','Q','K']:
            return 10
        return int(self.valor)
    
    def mostrar_carta(self):
        return self.pinta, self.valor

class CartaFrancesa(Carta):
    pass
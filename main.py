
import sys
from juego import *

j = Juego(MazoEspanol())
j.iniciar_juego()
j.jugar()
j.valorar_juego()

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("21 juego")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    


    pygame.display.flip()
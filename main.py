import pygame 
import sys
from juego import *

j = Juego(MazoEspanol())
j.iniciar_juego()
j.jugar()
ganador = j.valorar_juego()
print(ganador)

pygame.init()

COLOR_FONDO =(19, 92, 37)
WIDTH, HEIGTH = 800, 600
FONT = pygame.font.SysFont("Verdana", 24)

def dibujar_carta(carta,x,y,oculta):
    CARTA_OCULTA = pygame.transform.scale((pygame.image.load('Baraja_Espanola\Carta.jpeg')),(100,139))
    if oculta:
        screen.blit(CARTA_OCULTA,(x,y))
    else:
        screen.blit(carta.imagen,(x,y))

def dibujar_texto(texto,x,y):

    text_render = FONT.render(texto, True,'black')
    text_rect = text_render.get_rect()
    text_rect.topleft = (x,y)
    screen.blit(text_render,text_rect)

def dibujar_boton(rectangulo,texto,color):

    pygame.draw.rect(screen, color, rectangulo)
    texto = FONT.render(texto, True, 'black')
    texto_rect = texto.get_rect(center=rectangulo.center)
    screen.blit(texto, texto_rect)


def dibujar_baraja(baraja, oculta=False):
    x = 50

    if baraja == j.Casa.cartas:
        y=50
        dibujar_texto("Casa",x,y-35)
    else:
        y=350
        dibujar_texto("Jugador",x,y-35)

    for carta in baraja:
        dibujar_carta(carta, x, y,oculta)
        x += 60 + 10


screen = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("21 juego")
boton_rect = pygame.Rect(500,500,200,50)
boton_rect2 = pygame.Rect(WIDTH/2,HEIGTH/2,300,150)
OCULTA = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(event.pos):
                OCULTA = False
    
    screen.fill(COLOR_FONDO)
    
    dibujar_baraja(j.Casa.cartas) 
    dibujar_baraja(j.Jugador.cartas,OCULTA)

    dibujar_boton(boton_rect,"mostrar cartas",'gray')

    if OCULTA == False:
        if ganador:
            dibujar_boton(boton_rect2,"JUGADOR GANA",'red')
        else:
            dibujar_boton(boton_rect2,"CASA GANA",'red')

    pygame.display.flip()
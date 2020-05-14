import pygame
from pygame.locals import *
import sys

#Iniciación de Pygame
pygame.init()

#Pantalla - ventana
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Exterminator")
icono=pygame.image.load("icon.png")
pygame.display.set_icon(icono)


#Fondo del juego
fondo = pygame.image.load('ciudad.png')

#Personaje
quieto = pygame.image.load('idle1.png')

caminaDerecha = [pygame.image.load('run1.png'),
                 pygame.image.load('run2.png'),
                 pygame.image.load('run3.png'),
                 pygame.image.load('run4.png'),
                 pygame.image.load('run5.png'),
                 pygame.image.load('run6.png')]

caminaIzquierda = [pygame.image.load('run1-izq.png'),
                   pygame.image.load('run2-izq.png'),
                   pygame.image.load('run3-izq.png'),
                   pygame.image.load('run4-izq.png'),
                   pygame.image.load('run5-izq.png'),
                   pygame.image.load('run6-izq.png')]

salta = [pygame.image.load('jump1.png'),
         pygame.image.load('jump2.png')]

x=0
px = 50
py = 200
ancho = 40
velocidad = 10

#Control de FPS
reloj = pygame.time.Clock()

#Variables salto
salto = False
#Contador de salto
cuentaSalto = 10

#Variables dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    #Contador de pasos
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0
    #Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

        # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 2:
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

    #Actualización de la ventana
    pygame.display.update()


ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    reloj.tick(18)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
    #Tecla SPACE - Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()
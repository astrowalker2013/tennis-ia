# Ping Pong V1

import sys, pygame
from pygame.locals import *

pygame.init()


import pygame
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame

pygame.init()

ecran = pygame.display.set_mode((800,800))
balle = pygame.image.load("intro_ball.gif").convert()
ecran.blit(balle,(400,400))
raquetteD=  pygame.image.load("raquette.jpg").convert()
ecran.blit (raquetteD,(0,0))
raquetteG=  pygame.image.load("raquette.jpg").convert()
ecran.blit (raquetteG,(770,0))
pygame.display.flip()

continuer = True

position_raquetteD = raquetteD.get_rect().move(0,0)
position_raquetteG = raquetteG.get_rect().move(770,0)
position_balle     =  balle.get_rect().move(400,400)

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                position_raquetteG = position_raquetteG.move(0,10)
            if event.key == K_UP:
                position_raquetteG = position_raquetteG.move(0,-10)
            if event.key == K_q:
                position_raquetteD = position_raquetteD.move(0, 10)
            if event.key == K_a:
                position_raquetteD = position_raquetteD.move(0, -10)




# Re-collage
    ecran = pygame.display.set_mode((800, 800))
    ecran.blit(balle, (400, 400))
    ecran.blit(raquetteG, position_raquetteG)
    ecran.blit(raquetteD, position_raquetteD)
# Rafraichissement
    pygame.display.flip()
pygame.quit()
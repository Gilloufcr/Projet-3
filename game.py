# -*-coding:Utf-8 -*
"""Fichier Principal du jeux de labyrinthe a terminer..."""

import os
import pygame
from pygame.locals import *
from constancy import *
from clevel import Level
from ccaracter import Caracter

pygame.init()
game_on = True
menu_choice = ""

#Open Pygame Windows 
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

#Title of Windows
pygame.display.set_caption(titre_fenetre)

while game_on == True:
    """Tant que la partie n'est pas fini, on a atteint la sortie G"""
    
    """Menu"""

    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

	#Rafraichissement
    pygame.display.flip()
            
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    wait_choice = True

    while wait_choice:
        for event in pygame.event.get():
            if event.type == KEYDOWN: 
                if event.key == K_F1:
                    wait_choice = False
                    level_choice = '1'

                elif event.key == K_F2:
                    wait_choice = False
                    level_choice = '2'
    
    list_of_objects = []

    #Chargement du fond
    fond = pygame.image.load(image_fond).convert()

    play_level = Level(level_choice)
    play_level.display_level(fenetre)
    macgiver = Caracter("images/dk_droite.png", play_level)

    while macgiver.end is not True:

        
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        wait_move = True
        while wait_move:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    macgiver.move(event.key)
                    fenetre.blit(fond, (0,0))
                    #fenetre.blit(dk.direction, (dk.x, dk.y))
                    play_level.display_level(fenetre, macgiver.position_0)
                
                    pygame.display.flip()
                
    
    game_on = False
        
    
       
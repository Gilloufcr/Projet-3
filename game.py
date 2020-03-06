# -*-coding:Utf-8 -*
"""Main File of Game"""

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
    """Until the end game we do a while"""
    
    """Menu"""

    #Display game screen
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    pygame.time.Clock().tick(30)

    #Wait level choice of player 
    wait_choice = True

    while wait_choice:
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                wait_choice = False
                game_on = False

            elif event.type == KEYDOWN: 
                if event.key == K_F1:
                    wait_choice = False
                    level_choice = '1'

                elif event.key == K_F2:
                    wait_choice = False
                    level_choice = '2'
    
    list_of_objects = []

    #Background load
    background = pygame.image.load(image_fond).convert()

    play_level = Level(level_choice)
    play_level.display_level(fenetre)
    macgiver = Caracter("images/MacGyver.png", play_level)

    while macgiver.end == "":

        
        pygame.time.Clock().tick(30)
        
        while macgiver.wait_move:
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    game_on = False
				
                elif event.type == KEYDOWN:
                    macgiver.move(event.key)
                    fenetre.blit(background, (0,0))
                    play_level.display_level(fenetre, macgiver.position_0)
                
                    pygame.display.flip()
                

    if macgiver.end == "win":
        print("je suis la ")
        end = pygame.image.load(image_win).convert()
        fenetre.blit(end, (0,0))
        pygame.display.flip()
        pygame.time.Clock().tick(30)
    
    game_on = False
        
    
       
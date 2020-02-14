# -*-coding:Utf-8 -*
"""Fichier Principal du jeux de labyrinthe a terminer..."""

import os
from getkey import getkey, keys
from clevel import Level
from ccaracter import Caracter


game_on = True
menu_choice = ""


while game_on == True:
    """Tant que la partie n'est pas fini, on a atteint la sortie G"""
    
    """Menu"""
    menu_choice = input("Merci de faire un choix : \n 1-)Selection du niveau, 1, 2, 3 \n 2-)Quitter \n\nVotre choix : ")
        
    if menu_choice == '1':
    
        level_choice = input("Merci de Choisir une cartes parmis la liste suivante 1,2,3 : ")
            
        play_level = Level(level_choice)
        play_level.display_level()
        macgiver = Caracter(play_level)

        list_of_objects = []
        while macgiver.end is not True:
            macgiver.move(getkey())
            play_level.display_level(macgiver.position_0)
            
            print(macgiver.objects)
            
        
        game_on = False
        
    if menu_choice == '2':
        game_on = False
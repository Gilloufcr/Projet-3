# -*-coding:Utf-8 -*

from pathlib import Path
from ccaracter import Caracter
import random
import os
import pygame
from pygame.locals import *
from constancy import *

mon_rep_cartes = Path(__file__).parent / "cartes"
cartes_temp = Path(__file__).parent / "temp"

class Level():
    
    def __init__(self, maps):
        self.maps = maps
        self.positionmc = (-1, -1)
        self.wall = []
        self.guardian = []
        self.spaces = []
        self.first_elements_position = {}
        self.dict_objects = {}
        self.list_level = []
        self.create_level(self.maps)
       
    def create_level(self, maps):
        with open(str(mon_rep_cartes) + "/" + maps + ".txt", 'r') as contenu:
            level = contenu.read()
            for i, line in enumerate(level.splitlines()):
                list_line = []
                for j, elements in enumerate(line):
                    if elements == "X":
                        self.positionmc = (j, i)
                        self.spaces.append((j, i))
                    elif elements == "O":
                        self.wall.append((j,i))
                    elif elements == "G":
                        self.guardian.append((j,i))
                    elif elements == " ":
                        self.spaces.append((j,i))
 
                    list_line.append(elements)
                
                self.list_level.append(list_line)

            position_P = random.choice(self.spaces)
            del self.spaces[self.spaces.index(position_P)]
            position_N = random.choice(self.spaces)
            del self.spaces[self.spaces.index(position_N)]
            position_E = random.choice(self.spaces)
            del self.spaces[self.spaces.index(position_E)]
            self.dict_objects[position_P] = ("P")
            self.dict_objects[position_N] = ("N")
            self.dict_objects[position_E] = ("E")
            #print(self.dict_objects)
            for key in self.dict_objects.keys():
                self.list_level[key[1]][key[0]] = self.dict_objects[key]  

        return self.list_level        
    
    def display_level(self, fenetre, positionmac=()):
       # clear = lambda: os.system('clear')
       # clear()

        mur = pygame.image.load(image_mur).convert()
        gardien = pygame.image.load(image_arrivee).convert_alpha()
        mac = pygame.image.load(MacGyver).convert_alpha()
        needle = pygame.image.load(picture_needle).convert_alpha()
        ether = pygame.image.load(picture_ether).convert_alpha()
        pipe = pygame.image.load(picture_pipe).convert_alpha()


        if positionmac != ():
            self.list_level[self.positionmc[1]][self.positionmc[0]] = " "
            self.list_level[positionmac[1]][positionmac[0]] = "X"
            self.positionmc = positionmac

        num_ligne = 0
        for line in self.list_level:
            num_case = 0
            for elements in line:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if elements == 'O':		   
                    fenetre.blit(mur, (x,y))
                elif elements == 'G':		   
                    fenetre.blit(gardien, (x,y))
                elif elements == 'X':
                    fenetre.blit(mac, (x,y))
                elif elements == 'P':
                    fenetre.blit(pipe, (x,y))
                elif elements == 'E':
                    fenetre.blit(ether, (x,y))
                elif elements == 'N':
                    fenetre.blit(needle, (x,y))
                
                num_case += 1
            num_ligne += 1
            
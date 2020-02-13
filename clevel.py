# -*-coding:Utf-8 -*

from pathlib import Path
from ccaracter import Caracter
import random
import os

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
    
    def display_level(self, positionmac=()):
        clear = lambda: os.system('clear')
        clear()
        if positionmac != ():
            self.list_level[self.positionmc[1]][self.positionmc[0]] = " "
            self.list_level[positionmac[1]][positionmac[0]] = "X"
            self.positionmc = positionmac

        for line in self.list_level:
            line_to_display = ""
            for elements in line:
                line_to_display += elements
            print(line_to_display)
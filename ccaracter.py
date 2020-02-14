# -*-coding:Utf-8 -*

from getkey import getkey, keys

class Caracter():

    def __init__(self, level_game):

        self.position_0 = level_game.positionmc
        self.position_wall = level_game.wall
        self.position_guardian = level_game.guardian
        self.position_spaces = level_game.spaces
        self.level_game = level_game
        self.new_positionmc = (0, 0)
        self.objects = []
        self.end = False
        print("Position of Mac when Level Is Created", self.position_0)
        


    def move(self, key):
        
        x,y = self.position_0
        objects = ""        
        if key == keys.UP:
            print("Position in UP time", self.position_0)
            self.new_positionmc = (x,y-1)
                       
        elif key == keys.DOWN:
            print("Position in DOWN time", self.position_0)
            self.new_positionmc = (x,y+1)
        
        elif key == keys.RIGHT:
            print("Position in RIGHT time", self.position_0)
            self.new_positionmc = (x+1,y)
            
        elif key == keys.LEFT:
            print("Position in LEFT time", self.position_0)
            self.new_positionmc = (x-1,y)
        else:
            self.new_positionmc = x, y    
            
        if self.new_positionmc in self.position_spaces:
            self.position_0 = self.new_positionmc
            self.position_spaces.append(self.position_0)
        elif self.new_positionmc in self.level_game.dict_objects.keys():
            self.objects.append(self.level_game.dict_objects[self.new_positionmc])
            del self.level_game.dict_objects[self.new_positionmc]
            self.position_spaces.append(self.new_positionmc)
            self.position_0 = self.new_positionmc
            print(objects)
        
        if self.new_positionmc in self.position_guardian:
            if len(self.objects) == 3:
                self.end = True
                print("Vous avez Gagné!")
            else:
                self.end = True
                print("Vous avez perdu!!")


        return self.end
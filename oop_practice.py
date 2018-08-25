# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Soldier:
    
    "A WWII Soldier"
    def __init__(self, name, rank, allegiance):
        self.name=name
        self.rank=rank
        self.allegiance=allegiance
        self.health=100
        self.status="Alive and Well"
        
        
    
    def equip(self):
        if(self.allegiance=="German"):
            self.primary_weapon="KAR98"
        elif(self.allegiance=="Soviet"):
            self.primary_weapon="M1891"
        elif(self.allegiance=="American"):
            self.primary_weapon="M1 Garand"
        elif(self.allegiance=="Japanese"):
            self.primary_weapon="Arisaka"
        else:
            self.primary_weapon="Lee-Enfield"
            
            
    def axis(self):
        if (self.allegiance=="German" or self.allegiance=="Japanese"):
            return True
        else:
            return False
        
    def shot(self):
        self.health=self.health-30
        self.status="Wounded-Shot"
        if(self.health <= 0):
            self.status="Dead"
    
    def contact(self, another_soldier):
        if(not(self.axis() and another_soldier.axis())):
            another_soldier.shot()
    
    
class Scout(Soldier):
    def equip(self):
        self.primary_weapon="Side Arm"
        

        
        
     
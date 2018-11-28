# -*- coding: utf-8 -*-
"""
Author: Travis Asher
Date: 11/27/18
Purpose: Defines the class 'DnD_Character', which includes their stats and various functions
"""

import numpy as np
import random as rand


class DnD_Character:
    '''Creates an object of the DnD Character type. This includes their natural statistics.'''
    
    def __init__(self,strength=0,dexterity=0,constitution=0,intelligence=0,wisdom=0,charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    
    def get_stats(self):
        print("Str: {} | Dex: {} | Con: {} | Int: {} | Wis: {} | Cha: {}\n".format(self.strength,self.dexterity,
              self.constitution,self.intelligence,self.wisdom,self.charisma))
        
    def reroll_stats(self):
        dice = []
        for di in range(1,5):
            roll = rand.randint(1,6)
            dice.append(roll)
        #Discards lowest roll
        dice.remove(min(dice))
        return(dice)
        
# -*- coding: utf-8 -*-
"""
Author: Travis Asher
Date: 11/27/18
Purpose: Defines the class 'DnD_Character', which includes their stats and various functions
"""

import numpy as np
import random as rand
import re #imports regular expressions


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
        
    def reroll_stats(self,stat='',all_stats=False):
        '''This function rerolls either a certain statistic for your character or all of your character's\
 statistics at the same time. By default, 'all_stats' is False, meaning that your input need only include\
 either the abbreviation for the stat you wish to reroll or the stat's full name. If 'all_stats' is set to be\
 True, then the 'stat' input is ignored and rerolls are applied to each statistic.'''
 
        stat_list = ['strength','str','dexterity','dex','constitution','con','intelligence','int','wisdom',
                     'wis','charisma','cha']
        if all_stats==True:
        #First, we must generate a valid stat list from our stat_list that includes abbreviations:
            valid_stat_list = []
            for item in stat_list: 
                if len(item)>3: 
                    valid_stat_list.append(item)
            for item in valid_stat_list:
                dice = []
                for di in range(1,5):
                    roll = rand.randint(1,6)
                    dice.append(roll)
                dice.remove(min(dice)) #Discards lowest roll
                sum_dice = sum(dice)
                setattr(self,item,sum_dice)
            print("Your new stats are:\n  ")
            self.get_stats()
        else:  
            if stat == '':
                print("You must indicate a statistic that you wish to reroll on. Acceptable input includes either\
 the full name of the statistic that you wish to reroll or its first three letter abbreviation.\n")
            elif stat in stat_list:
                dice = []
                for di in range(1,5):
                    roll = rand.randint(1,6)
                    dice.append(roll)
                dice.remove(min(dice)) #Discards lowest roll
                sum_dice = sum(dice)
                if len(stat)==3:
                    stat=stat_list[stat_list.index(stat)-1] #If using the abbreviation for stats, then this line
                                                            # adjusts 'stat' to the full name for the next function
                setattr(self,stat,sum_dice)
                print("Your new '{}' is '{}'.\n".format(stat,sum_dice))
            else:
                print("Your input isn't acceptable. Acceptable input includes either the full name of the statistic\
 that you wish to reroll or its first three letter abbreviation.\n")
            
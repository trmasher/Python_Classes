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
    
    def __init__(self,race='Human',char_class='Fighter',strength=0,dexterity=0,constitution=0,intelligence=0,wisdom=0,charisma=0):
        self.race = race
        self.char_class = char_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    
    
#We force 'race' to be of the acceptable DnD races:
    def auto_race(self):
        return self._r
    
    def set_race(self, race):
        race_list = ['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Tiefling']
        if race not in race_list:
        #Before moving along, we perform a check to see if the input is just the lowercase of the valid races:
            bool_check = []
            for item in race_list:
                state = race == item.lower()
                bool_check.append(state)
            if True not in bool_check:
                raise ValueError("Your race is not a valid DnD race. Valid race inputs include: {}.".format(race_list))
        self._r = race.capitalize()

    race = property(auto_race,set_race)
    
    
#We force 'char_class' to be of the acceptable DnD classes:
    def auto_char_class(self):
        return self._cl
    
    def set_char_class(self, char_class):
        class_list = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer',
                      'Warlock','Wizard']
        if char_class not in class_list:
        #Before moving along, we perform a check to see if the input is just the lowercase of the valid classes:
            bool_check = []
            for item in class_list:
                state = char_class == item.lower()
                bool_check.append(state)
            if True not in bool_check:
                raise ValueError("Your class is not a valid DnD class. Valid class inputs include: {}.".format(class_list))
        self._cl = char_class.capitalize()

    char_class = property(auto_char_class,set_char_class)
    
    
#We define various useful methods for you to perform on your character:
    def get_stats(self):
        '''This method provides an asthetic way of outputting your character's six statistics' values.'''
        print("Str: {} | Dex: {} | Con: {} | Int: {} | Wis: {} | Cha: {}\n".format(self.strength,self.dexterity,
              self.constitution,self.intelligence,self.wisdom,self.charisma))
        
        
    def reroll_stats(self,stat='',all_stats=False):
        '''This method rerolls either a certain statistic for your character or all of your character's\
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
            
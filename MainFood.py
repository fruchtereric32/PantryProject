# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:23:08 2019

@author: ericp
"""
import CookingItem


##The class mainfood is used for the creation and keeping tracking of any foods considered a main\
##It is a subclass of CookingItem
class MainFood(CookingItem.CookingItem):
    ##The constructor here has the ability to take a qty but generally we know it won't have one
    ##This is why we prompt the users to enter how many mains they are adding of this type
    def __init__(self,fi,qt=0):
        if qt == 0:
            qt=input("How many pieces are in the pack? (Default to 1)")
        try:
            qt = int(qt)
        except ValueError:
            qt = 1
        if qt < 1:
            qt = 1
        super().__init__(fi,qt)
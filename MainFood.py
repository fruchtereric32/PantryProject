# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:23:08 2019

@author: ericp
"""
import CookingItem

class MainFood(CookingItem.CookingItem):
    def __init__(self,fi,qt=0):
        if qt == 0:
            qt=input("How many pieces are in the pack?")
        super().__init__(fi,qt)
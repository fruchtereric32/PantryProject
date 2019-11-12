# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:49:21 2019

@author: ericp
"""
import CookingItem

##The class spice is used for the creation and keeping tracking of any foods considered an ingredient (not main)
##It is a subclass of CookingItem
class Spice(CookingItem.CookingItem):
    def __init__(self, itm, msr):
        super().__init__(itm, msr)
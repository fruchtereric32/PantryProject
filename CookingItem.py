# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:08:10 2019

@author: ericp
"""

class CookingItem:
    def __init__(self, item, amount=1):
        self.item = item
        self.amount = amount
        print("New item {0} has been added created with a qty of {1}!".format(item,str(amount)))
    
    def reduce_amt(self, amount_used):
        self.amount -= amount_used
        print("You selected to use {au} of your {it}. You have {al}".format(au=amount_used, it=self.item, al=self.amount))
    
    def add_amnt(self):
        qty_to_add = ""
        while len(qty_to_add) == 0:
            qty_to_add = input("How much {0} would you like to add to your pantry?:".format(self.item))
        self.amount += int(qty_to_add)
        print("You selected to add {ab} of your {it}. You have {al}".format(ab=qty_to_add, it=self.item, al=self.amount))    
 
    def enough_left(self, amount_needed):
        return self.amount >= amount_needed
    
    def get_item(self):
        return self.item, self.amount
 
    def get_item_name(self):
        return self.item
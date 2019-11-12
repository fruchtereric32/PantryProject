# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:08:10 2019

@author: ericp
"""
##The class CookingItem is the base behind the whole project.
##It contains the main functionality behind mains and all ingredients
class CookingItem:
    ##The constructor here simply assigns the item name and qty defaulting to 1 if not provided
    def __init__(self, item, amount=1):
        self.item = item
        self.amount = amount
        print("New item {0} has been added created with a qty of {1}!".format(item,str(amount)))
    
    ##The reduce_amt fucntion is used for when a user uses items and they can choose to reduce the item
    ##We hope to automatically have this happen when they decide to use a recipe in the future
    def reduce_amt(self, amount_used):
        self.amount -= amount_used
        print("You selected to use {au} of your {it}. You have {al}".format(au=amount_used, it=self.item, al=self.amount))
    
    ##The add_amnt functionality is used if an item already exists in the pantry and you bought more
    ##We prompt the user for how much more they want to add and add it to the previous amount already stored
    def add_amnt(self):
        qty_to_add = ""
        while len(qty_to_add) == 0:
            qty_to_add = input("How much {0} would you like to add to your pantry?:".format(self.item))
        self.amount += int(qty_to_add)
        print("You selected to add {ab} of your {it}. You have {al}".format(ab=qty_to_add, it=self.item, al=self.amount))    
 
    ##The enough_left function will be used when a user selects a recipe 
    ##and we want to make sure we have enough of the item to make the recipe
    def enough_left(self, amount_needed):
        return self.amount >= amount_needed
    
    ##The get_item function returns a combination of the item name and amount
    def get_item(self):
        return self.item, self.amount
 
    ##The get_item_name function returns just the item name
    def get_item_name(self):
        return self.item
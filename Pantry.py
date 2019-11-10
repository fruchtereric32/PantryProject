# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:00:10 2019

@author: ericp
"""

import MainFood
import Spice
import requests
import DietaryOptions
import ApiRequestBuilder

class Pantry():
    def __init__(self, name):
        self.name = name
        self.mains=[]
        self.spices=[]
    
    def get_name(self):
        return self.name
    
    def add_main(self, cm, qt=0):
        for mn in self.mains:
            m_mn, m_qty = mn.get_item()
            if m_mn == cm:
                mn.add_amnt()
                return
        self.mains.append(MainFood.MainFood(cm, qt))
    
    def add_spice(self, sp_name, sp_amt):
        for sp in self.spices:
            s_mn, s_qty = sp.get_item()
            if s_mn == sp_name:
                sp.add_amnt()
                return
        self.spices.append(Spice.Spice(sp_name,sp_amt))
        
    def add_item(self, main_or_side):
        item_adding = ""
        while len(item_adding) == 0:
            item_adding = ""
            while len(item_adding) == 0:
                item_adding = input("What item are you adding to the pantry?")
        if main_or_side == 'S':
            num_bought = None
            try:
                num_bought = input("How many of this spice did you buy? (Deafult to 1)")
                num_bought = int(num_bought)
            except ValueError:
                num_bought = 1
            if num_bought < 1:
                num_bought = 1
            self.add_spice(item_adding, num_bought)
        else:
            self.add_main(item_adding)
                
        
    def look_for_recipe(self):
        print("Here are a list of items that are in your pantry")
        print("Mains")
        for cnt in range(len(self.mains)):
            print("Option {optn}: You have {qty} number of {itm}".format(optn=cnt, qty=self.mains[cnt].amount, itm=self.mains[cnt].item))
        
        food_to_use = input("Which food would you like to make a meal out of? (Enter the option number):\n")
        print("Finding recipes with your restrictions for {0}".format(self.mains[int(food_to_use)].item))
        
        diet_options=DietaryOptions.get_diet_options()
        print(diet_options)
        l_cal, h_cal = DietaryOptions.set_calorie_range()
        filter_num = DietaryOptions.set_filter_counter()
        
        ApiRqst = ApiRequestBuilder.ApiRequestBuilder(self.mains[int(food_to_use)].item, diet_options, l_cal, h_cal, filter_num)
        potential_recipe = requests.get(ApiRqst.get_api_string())
        if potential_recipe.json()['count'] == 0:
            print("Unforuantely we couldn't find any matches for you! Try changing your preferences")
            return
        recipes = potential_recipe.json()['hits']
        for rcp in recipes:
            print(rcp['recipe']['label'])
            print(rcp['recipe']['ingredientLines'])
            print("\n\n")
            
    def print_items(self):
        print("Here are a list of items that are in your pantry")
        print("Mains")
        for cnt in range(len(self.mains)):
            print("You have {qty} number of {itm}".format(qty=self.mains[cnt].amount, itm=self.mains[cnt].item))
        print("Ingredients")
        for spc in self.spices:
            s_itm, s_qty = spc.get_item()
            print("You have {qty} number of {itm}.".format(qty=s_qty, itm=s_itm))
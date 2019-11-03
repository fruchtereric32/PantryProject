# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:00:10 2019

@author: ericp
"""

import CookingItem
import MainFood
import Spice
import requests

class Pantry():
    def __init__(self, name):
        self.name = name
        self.mains=[]
        self.spices=[]
    
    def add_main(self, cm, qt=0):
        self.mains.append(MainFood.MainFood(cm, qt))
    
    def add_spice(self, sp_name, sp_amt):
        self.spices.append(Spice.Spice(sp_name,sp_amt))
        
    def look_for_recipe(self):
        print("Here are a list of items that are in your pantry")
        print("Mains")
        for cnt in range(len(self.mains)):
            print("Option {optn}: You have {qty} number of {itm}".format(optn=cnt, qty=self.mains[cnt].amount, itm=self.mains[cnt].item))
        
        food_to_use = input("Which food would you like to make a meal out of? (Enter the option number):\n")
        print("Finding recipes with your restrictions for {0}".format(self.mains[int(food_to_use)].item))
        potential_recipe = requests.get("https://api.edamam.com/search?q={main}&app_id=ab4bf454&app_key=80971399f1f660312ba74b72ad419237&from=0&to=20&calories=591-722&health=peanut-free&health=tree-nut-free".format(main=self.mains[int(food_to_use)].item))
        print(potential_recipe.json()['hits'])
        recipes = potential_recipe.json()['hits']
        for rcp in recipes:
            print(rcp['recipe']['label'])
            print(rcp['recipe']['ingredientLines'])
            print("\n\n")

Home=Pantry("home")
Home.add_main("Chicken".lower(),2)

Home.add_spice("Paprika".lower(), 5)


Home.look_for_recipe()


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
import Recipe
import os

##The class Pantry will be used to store items in the given pantry 
##and perform actions using those items
class Pantry():
    
    ##Used to keep track of how many Pantries there are
    counter = 0
    
    ##In the constructor, we create the pantry and create lists for mains and spices
    def __init__(self, name):
        self.name = name
        self.mains=[]
        self.spices=[]
        self.stored_recipes={}
        Pantry.counter+=1
    
    ##get_name returns the name of the pantry
    def get_name(self):
        return self.name
    
    ##add_main is used to add a main item to this pantry
    ##If we see the item is already in the main, we just use the add_amnt function to add to the qty
    ##If the item is not already in the pantry, we create a new main item 
    ##and add it to the mains list
    def add_main(self, cm, qt=0):
        for mn in self.mains:
            m_mn, m_qty = mn.get_item()
            if m_mn == cm:
                mn.add_amnt()
                return
        n_main = MainFood.MainFood(cm,qt)
        self.mains.append(n_main)
    
    ##add_spice works exactly as add_main except for spices (non-mains)
    def add_spice(self, sp_name, sp_amt):
        for sp in self.spices:
            s_mn, s_qty = sp.get_item()
            if s_mn == sp_name:
                sp.add_amnt()
                return
        self.spices.append(Spice.Spice(sp_name,sp_amt))
    
    ##The add_item function is the one called from teh main menu
    ##Depending on what's passed along, the fucntion will call the appropriate internal function
    ##It will before that prompt for the item being added and in case of a spice, will request qty
    ##Default qty will always be 1
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
                
    ##The look_for_recipe function takes in the provided main item.
    ##It then looks at the dietary options set before and calls the API functionality to get recipes
    ##If nothing is found, we apologize and recommend changing the dietary options
    ##Otherwise, we store the recipes into an array and print out the information for the recipe    
    def look_for_recipe(self,main_food):
        self.stored_recipes.clear()
        print("Finding recipes with your restrictions for {0}".format(main_food))
        
        diet_options=DietaryOptions.get_diet_options()
        h_cal, l_cal = DietaryOptions.get_calorie_options()
        filter_num = DietaryOptions.get_filter_counter()
        
        ApiRqst = ApiRequestBuilder.ApiRequestBuilder(main_food, diet_options, l_cal, h_cal, filter_num)
        potential_recipe = requests.get(ApiRqst.get_api_string())
        if potential_recipe.json()['count'] == 0:
            print("Unforuantely we couldn't find any matches for you! Try changing your preferences")
            return
        recipes = potential_recipe.json()['hits']
        num = 0
        for rcp in recipes:
            num += 1
            n_recipe = Recipe.Recipe(rcp['recipe'])
            self.stored_recipes[str(num)]=n_recipe
            print(n_recipe)
        print("Recipes Retrieved and Stored! Use the Main Menu to Look at Them")
    
    
    ##The select_main_to_use shows a user a list of all mains in the pantry
    ##It then asks the user to choose which item they want to select for now
    def select_main_to_use(self):
        print("Here are a list of items that are in your pantry")
        print("Mains")
        for cnt in range(len(self.mains)):
            print("Option {optn}: You have {qty} number of {itm}".format(optn=cnt, qty=self.mains[cnt].amount, itm=self.mains[cnt].item))
        
        food_to_use = input("Which food would you like to make a meal out of? (Enter the option number):\n")
        return self.mains[int(food_to_use)]
            
    ##The print_items function displays to the user a list of all mains and spices in the pantry
    def print_items(self):
        print("Here are a list of items that are in your pantry")
        print("Mains")
        for cnt in range(len(self.mains)):
            print("You have {qty} number of {itm}".format(qty=self.mains[cnt].amount, itm=self.mains[cnt].item))
        print("Ingredients")
        for spc in self.spices:
            s_itm, s_qty = spc.get_item()
            print("You have {qty} number of {itm}.".format(qty=s_qty, itm=s_itm))
            
    ##The function has_selected_recipes let's users know if they have any stored selected recipes
    def has_selected_recipes(self):
        print(len(self.stored_recipes))
        if len(self.stored_recipes) == 0:
            return "False"
        else:
            return "True"
    
    ##The function select_recipe dislays recipes stored 
    ##for selection at the increment requested by users
    def select_recipe(self, interval_num=5):
        for cnt, rcp in self.stored_recipes.items():
            print("Option {0}".format(cnt))
            print("============")
            print(rcp)
            
            int_cnt = int(cnt)
            
            if int_cnt%interval_num == 0 \
            or int_cnt == len(self.stored_recipes):
                choice = "-1"
                if int_cnt%interval_num == 0:
                    options = [str(i) for i in range(int_cnt - interval_num, int_cnt + 1)]
                    if len(self.stored_recipes) != int_cnt:
                        options.append('N')
                else:
                    options = [str(i) for i in range(int_cnt - (int_cnt%interval_num), int_cnt +1)]
                options.append('Q')
                while choice not in options:
                    print("Please select one of the above options by it's number, 'N' for the next set or 'Q' to Quit:")
                    choice = input("Enter Choice:")
                if choice.upper() == 'N':
                    os.system("clear")
                    print("Getting Next Recipes..")
                    continue
                elif choice.upper() == 'Q':
                    os.system("clear")
                    print("Going Back to Main Menu")
                    return False
                else:
                    print("Recipe Selected!")
                    choice = int(choice)
                    self.selected_recipe_index = choice
                    return True
                
    ##The function get_selected_recipe returns the selected Recipe
    def get_selected_recipe(self):
        return self.stored_recipes[str(self.selected_recipe_index)]
                
                    
    ##The static function pantry_count returns how many pantries there are right now
    @staticmethod
    def pantry_count():
        return Pantry.counter
    
        
            
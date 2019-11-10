# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:25:01 2019

@author: ericp
"""
import os
import Pantry
import DietaryOptions

class MainMenu:
    def __init__(self):
        self.selectedPantry = None
        self.selectedMain = None
        self.selectedDietRestrictions = None
        self.selectedFilterNumber = None
        self.low_calorie = 0
        self.high_calorie = 0
        self.pantries = []
        self.menu_options={
                "0":"Add New Pantry",
                "1":"Add New Main",
                "2":"Add New Ingredient",
                "3":"Set Dietary Restrictions", 
                "4":"Select main to use",
                "5":"Find Recipe", 
                "6":"Quit",
                "7":"Select Pantry to use",
                "8":"Print Pantry"}
    
    def launch(self):
        while True:
            self.selectedDietRestrictions = DietaryOptions.view_active_diet_options()
            self.high_calorie, self.low_calorie = DietaryOptions.get_calorie_options()
            self.selectedFilterNumber = DietaryOptions.get_filter_counter()
            
            if len(self.selectedDietRestrictions) == 0:
                self.selectedDietRestrictions = "None"
                
            print("     WELCOME TO YOUR PANTRY!")
            print("Let's find something for you to eat!")
            print("==========================================")
            try:
                print("Current Pantry: {0}".format(self.selectedPantry.get_name()))
            except AttributeError:
                print("Current Pantry: None")
            print("Current Main: {0}".format(self.selectedMain))
            print("Current DietRestrictions: {0}".format(self.selectedDietRestrictions))
            print("Current Filter Number: {0}".format(self.selectedFilterNumber))
            print("Low Calorie Setting: {0}".format(self.low_calorie))
            print("High Calorie Setting: {0}".format(self.high_calorie))
            print("==========================================")
            print("What would you like to do?")
            optn = None
            while optn not in ['0','1','2','3','4','5','6','7','8']:
                for k,v in self.menu_options.items():
                    print("{num_val}: {written_option}".format(num_val=k,written_option=v))
                optn = input("Press the number corresponding to the action you want to take:")
            if optn == '0':
                pantry_name = None
                while pantry_name == None:
                    pantry_name = input("Please enter a name for the new pantry: ")
                n_pantry = Pantry.Pantry(pantry_name)
                self.pantries.append(n_pantry)
                make_default_pantry = input("Would you like this to be your default pantry? (Default to Yes):")
                if len(make_default_pantry) == 0 or make_default_pantry[0].upper() == 'Y':
                    self.selectedPantry = n_pantry
            elif optn == '1':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before adding items")
                    continue
                else:
                    m_or_s = 'M'
                    self.selectedPantry.add_item(m_or_s)
            elif optn == '2':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before adding items")
                    continue
                else:
                    m_or_s = 'S'
                    self.selectedPantry.add_item(m_or_s)
            elif optn == '3':
                os.system("clear")
                DietaryOptions.set_diet_options()
            elif optn == "8":
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: No pantry selected to print")
                    continue
                else:
                    print("HERE!!!!")
                    self.selectedPantry.print_items()
            elif optn == '6':
                return
            elif optn == '7' and self.selectedMain == None:
                os.system("clear")
                print("ERROR: Please select a main from the pantry you want to use")
                continue
            
new_run = MainMenu()
new_run.launch()
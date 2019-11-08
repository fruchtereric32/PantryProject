# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:25:01 2019

@author: ericp
"""
import CookingItem
import os

class MainMenu:
    def __init__(self):
        self.selectedPantry = None
        self.selectedMain = None
        self.selectedDietRestrictions = None
        self.selectedFilterNumber = None
        self.low_calorie = 0
        self.high_calorie = 0
        self.menu_options={
                "0":"Add New Pantry",
                "1":"Add New Main",
                "2":"Add New Ingredient",
                "3":"Set Dietary Restrictions", 
                "4":"Set Calorie Levels", 
                "5":"Set Filter Retrieval Number",
                "6":"Select main to use",
                "7":"Find Recipe", 
                "8":"Quit"}
    
    def launch(self):
        while True:
            print("     WELCOME TO YOUR PANTRY!")
            print("Let's find something for you to eat!")
            print("==========================================")
            print("Current Pantry: {0}".format(self.selectedPantry))
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
            if optn == '8':
                return
            elif optn == '1' and self.selectedPantry == None:
                os.system('clear')
                print("ERROR: Please select a pantry first before adding items")
                continue
            elif optn == '2' and self.selectedPantry == None:
                os.system("clear")
                print("ERROR: Please select a pantry first before adding items")
                continue
            elif optn == '7' and self.selectedMain == None:
                os.system("clear")
                print("ERROR: Please select a main from the pantry you want to use")
                continue
            
new_run = MainMenu()
new_run.launch()
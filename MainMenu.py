# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:25:01 2019

@author: ericp
"""
import os
import Pantry
import DietaryOptions
import DatabaseConnector
import ActiveUser

##This class MainMenu is exactly what it sounds like
##It's the operating menu for all functionality
##We stored all teh selected items and filter settings
##and then display them to the user along with 9 options of things to do
#We keep it in a while loop until the user quits
class MainMenu:
    def __init__(self):
        self.selectedPantry = None
        self.selectedMain = None
        self.selectedDietRestrictions = None
        self.selectedFilterNumber = None
        self.currentRecipe = None
        self.low_calorie = 0
        self.high_calorie = 0
        self.pantries = []
        self.menu_options={
                "Q":"Quit",
                "1":"Add New Pantry",
                "2":"Add New Main",
                "3":"Add New Ingredient",
                "4":"Set Dietary Restrictions", 
                "5":"Select Pantry to use",
                "6":"Select Main to use",
                "7":"Find Recipe", 
                "8":"Print Pantry",
                "9":"Select Recipe",
                "0": "Display Current Recipe Info"}
        self.db = DatabaseConnector.DatabaseConnector()

    
    def launch(self):
        self.db.query("Select id,default_pantry,default_max_calories,default_min_calories from users")
        currentUser = ActiveUser.ActiveUser(self.db.return_response())

        while True:
            self.selectedDietRestrictions = DietaryOptions.view_active_diet_options()
            self.high_calorie, self.low_calorie = DietaryOptions.get_calorie_options(currentUser)
            self.selectedFilterNumber = DietaryOptions.get_filter_counter()
            self.selectedPantry = Pantry.Pantry("load", currentUser.get_user_id(), self.db, "blah")
            
            if len(self.selectedDietRestrictions) == 0 or self.selectedDietRestrictions == "None":
                self.selectedDietRestrictions = "None"
                
            print("     WELCOME TO YOUR PANTRY!")
            print("Let's find something for you to eat!")
            print("==========================================")
            try:
                print("Current Pantry: {0}".format(self.selectedPantry.get_name(self.db, currentUser.get_default_pantry())))
            except AttributeError:
                print("Current Pantry: None")
            
            try:
                print("Current Main: {0}".format(self.selectedMain.get_item_name()))
            except AttributeError:
                print("Current Main: None")
            print("Current DietRestrictions: {0}".format(self.selectedDietRestrictions))
            print("Current Filter Number: {0}".format(self.selectedFilterNumber))
            print("Low Calorie Setting: {0}".format(self.low_calorie))
            print("High Calorie Setting: {0}".format(self.high_calorie))
            if Pantry.Pantry.pantry_count() != 0 \
            and self.selectedPantry != None:
                print("Selected Recipes: {0}".format(self.selectedPantry.has_selected_recipes()))
            try:
                print("Current Recipe: {0}".format(self.currentRecipe.get_recipe_name()))
            except AttributeError:
                pass
            print("==========================================")
            print("What would you like to do?")
            optn = None
            while optn not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'q']:
                for k,v in self.menu_options.items():
                    print("{num_val}: {written_option}".format(num_val=k,written_option=v))
                optn = input("Press the number corresponding to the action you want to take:")
            if optn.upper() == 'Q':
                return
            elif optn == '1':
                pantry_name = None
                while pantry_name == None:
                    pantry_name = input("Please enter a name for the new pantry: ")
                n_pantry = Pantry.Pantry("new", currentUser.get_user_id(), self.db, pantry_name)
                self.pantries.append(n_pantry)
            elif optn == '2':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before adding items")
                    continue
                else:
                    m_or_s = 'M'
                    self.selectedPantry.add_item(m_or_s)
            elif optn == '3':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before adding items")
                    continue
                else:
                    m_or_s = 'S'
                    self.selectedPantry.add_item(m_or_s)
            elif optn == '4':
                os.system("clear")
                DietaryOptions.set_diet_options(currentUser, self.db)
            elif optn == '5':
                if len(self.pantries) == 0:
                    os.system("clear")
                    print("ERROR: There are no pantries currently created")
                    continue
                for pntry in range(len(self.pantries)):
                    print("{0}: {1}".format(pntry, self.pantries[pntry].get_name()))
                pntry_option = input("Please enter the associated number to the pantry you want (Default to first):")
                if len(pntry_option) == 0:
                    pntry_option = 0
                pntry_option = int(pntry_option)
                self.selectedPantry = self.pantries[pntry_option]
            elif optn == '6':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before trying to select an item")
                os.system("clear")
                self.selectedMain = self.selectedPantry.select_main_to_use()
            elif optn == '7':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before trying to find a recipe")
                elif self.selectedMain == None:
                    os.system("clear")
                    print("ERROR: Please select a main first before trying to find a recipe")
                else:
                    self.selectedPantry.look_for_recipe(self.selectedMain.get_item_name())
            elif optn == "8":
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: No pantry selected to print")
                    continue
                else:
                    self.selectedPantry.print_items()
            elif optn == '9':
                if self.selectedPantry == None:
                    os.system("clear")
                    print("ERROR: Please select a pantry first before pulling up recipes")
                    continue
                elif self.selectedPantry.has_selected_recipes() == "False":
                    os.system("clear")
                    print("ERROR: Please find recipes before pulling up recipes")
                else:
                    view_amount = input("How many items would you like to view at one time? (Default to 5):")
                    try:
                        view_amount = int(view_amount)
                    except ValueError:
                        view_amount = 1
                    selected_recipe = self.selectedPantry.select_recipe(view_amount)
                    if selected_recipe:
                        self.currentRecipe = self.selectedPantry.get_selected_recipe()
                    else:
                        self.currentRecipe = None
            elif optn == '0':
                if self.currentRecipe == None:
                    os.system("clear")
                    print("ERROR: Please select a Recipe first before attempting to read it")
                else:
                    print(self.currentRecipe)
                    launch_url = input("Would you like to launch the URL for this Recipe (Default to N):")
                    if len(launch_url) == 0:
                        launch_url = 'N'
                    if launch_url.upper()[0] == 'Y':
                        self.currentRecipe.launch_main_link()
            
new_run = MainMenu()
new_run.launch()

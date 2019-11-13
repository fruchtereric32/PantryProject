# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:23:54 2019

@author: ericp
"""
import requests

##This class will be used to store the important part of the recipes
class Recipe:
    ##The constructor for this class takes in the json string returned from the recipe
    ##and breaks it down to the parts we deem important to show in program
    def __init__(self, recipe_json):
        self.recipe_json = recipe_json
        self.recipe_name = recipe_json['label']
        self.ingredients = recipe_json['ingredientLines']
        self.directions_avail_url = recipe_json['url']
        self.endamam_url = recipe_json['shareAs']
        self.diet_labels = []
        self.diet_labels.append(recipe_json['dietLabels'])
        self.diet_labels.append(recipe_json['healthLabels'])
        self.cautions = recipe_json['cautions']     
        self.calories = recipe_json['calories']
        self.has_proper_recipe_link()
    
    ##The fucntion has_proper_recipe_link tests to it's best ability if the recipe
    ##has a link to go to the instructions on how to cook
    def has_proper_recipe_link(self):
        valid_code = requests.head(self.directions_avail_url, allow_redirects = True)
        if valid_code.status_code == 200:
            return True
        else:
            return False
    
    ##The function launch_main_link will be used to launch in the default browser the url
    ##for the recipe
    def launch_main_link(self):
        return self.endamam_url
    
    ##The function get_ingredients will return the list of ingredients
    def get_ingredients(self):
        return self.ingredients
    
    ##The function get_diet_labels will return the list of dietary settings in this recipe
    def get_diet_labels(self):
        return self.diet_labels
    
    ##The function get_cautions will return a list of cautionary items (may contains)
    def get_cautions(self):
        return self.cautions
    
    ##The functino get_calories will show the user the set calories in this recipe
    def get_calories(self):
        return self.calories
    
    ##The function get_recipe_name returns the stored recipe name
    def get_recipe_name(self):
        return self.recipe_name
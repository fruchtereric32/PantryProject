# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:19:17 2019

@author: ericp
"""

potential_diet_options={"Well Balanced":"balanced", "High Protein":"high-protein","Low Fat":"low-fat","Low Carb":"low-carb","Vegan":"vegan","Vegatarian":"vegetarian","Sugar Conscious":"sugar-conscious","Peanut Free":"peanut-free","Tree Nut Free":"tree-nut-free","Alcohol Free":"alcohol-free"}
select_diet_options= []

def get_diet_options():
    if len(select_diet_options) != 0:
        print("You have previously selected dietary options (See below)")
        for key,val in potential_diet_options.items():
            if val in select_diet_options:
                print(key)
        change_preferences=input("Would you like to change your settings? (Default to No)")
        if len(change_preferences) == 0 or change_preferences[0].upper() != 'Y':
            return select_diet_options
    
    select_diet_options.clear()
    
    for key,val in potential_diet_options.items():
        include_diet_option = 'N'
        include_diet_option = input("Would you like to make sure the meal is {0}?(Default to No)\n".format(key))
        try:
            if include_diet_option[0].upper() == 'Y':
                select_diet_options.append(val)
        except IndexError:
            include_diet_option = 'N'
    return select_diet_options
        
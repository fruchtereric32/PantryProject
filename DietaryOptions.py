# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:19:17 2019

@author: ericp
"""

potential_diet_options={"Well Balanced":{"balanced":False}, 
                        "High Protein":{"high-protein":False},
                        "Low Fat":{"low-fat":False},
                        "Low Carb":{"low-carb":False},
                        "Vegan":{"vegan":False},
                        "Vegatarian":{"vegetarian":False},
                        "Sugar Conscious":{"sugar-conscious":False},
                        "Peanut Free":{"peanut-free":False},
                        "Tree Nut Free":{"tree-nut-free":False},
                        "Alcohol Free":{"alcohol-free":False}}
filter_vars={"m_low_cal":0, "m_high_cal":10000, "m_base_number_returned":25}

def set_diet_options():
    print("You have previously selected dietary options (See below)")
    for key,val in potential_diet_options.items():
        for itm_nm, selected in val.items():
            print("{0} is set to {1}".format(key,selected))
    print("Calories: {0} - {1}".format(filter_vars["m_low_cal"], filter_vars["m_high_cal"]))
    print("Items to Return: {0}".format(filter_vars["m_base_number_returned"]))
    change_preferences=input("Would you like to change your settings? (Default to No)")
    if len(change_preferences) == 0:
        change_preferences = 'N'
    if change_preferences[0].upper() == 'N':
        return

    set_filter_counter()
    set_calorie_range()
    
    for key,val in potential_diet_options.items():
        for itm_nm, selected in val.items():
            include_diet_option = 'N'
            include_diet_option = input("Would you like to make sure the meal is {0}?(Default to {1})\n".format(key,selected))
            try:
                if include_diet_option[0].upper() == 'Y':
                    potential_diet_options[key][itm_nm] = True
                else:
                    potential_diet_options[key][itm_nm] = False
            except IndexError:
                potential_diet_options[key][itm_nm] = False
    
def get_diet_options(): 
    select_diet_options = []
    for key,val in potential_diet_options.items():
        s_key, s_val = val.items()
        if s_val == True:
            select_diet_options.append(s_key)
    return select_diet_options

def view_active_diet_options():
    selected_diet_option = ""
    for key,val in potential_diet_options.items():
        for s_key, s_val in val.items():
            if s_val == True:
                selected_diet_option += "\n\t{0}".format(key)
    return selected_diet_option
        
def set_calorie_range():
    low_cal = filter_vars["m_low_cal"]
    high_cal = filter_vars["m_high_cal"]
    if low_cal != 0 or high_cal != 10000:
        print("You currently have a calorie setting stored of the following:")
        if low_cal == None:
            low_cal = 0
        elif high_cal == None:
            high_cal = 10000
        print("Low: {0}".format(low_cal))
        print("High: {0}".format(high_cal))
        change_cal = input("Would you like to change these settings? (Default to No)\n")
        if len(change_cal) == 0:
            change_cal = 'N'
        else:
            change_cal = change_cal[0].upper()
        if change_cal != 'Y':
            return low_cal, high_cal
    else:
        low_cal = 0
        high_cal = 10000
        set_cal = input("The default settings do not care about calorie count.\nWould you like to set Lower/Upper limits? (Default to No)\n")
        if len(set_cal) == 0:
            set_cal = 'N'
        else:
            set_cal = set_cal[0].upper()
        if set_cal != 'Y':
            return low_cal, high_cal
    print("The lower calorie setting is currently set to {0}. Press Enter to keep it the same or enter a new numer".format(low_cal))
    c_low_cal = low_cal
    low_cal = input("Low Cal: {0} should be:".format(low_cal))
    if len(low_cal) == 0:
        low_cal = c_low_cal
    c_high_cal = high_cal
    high_cal = input("High Cal: {0} should be:".format(high_cal))
    if len(high_cal) == 0:
        high_cal = c_high_cal
    low_cal = int(low_cal)
    high_cal = int(high_cal)
    while low_cal > high_cal:
        c_low_cal = filter_vars["m_low_cal"]
        c_high_cal = filter_vars["m_high_cal"]
        print("The lower calorie setting can't be higher than the high calorie setting. Please try again")
        low_cal = input("Low Cal: {0} should be:".format(c_low_cal))
        if len(low_cal) == 0:
            low_cal = c_low_cal
        high_cal = input("High Cal: {0} should be:".format(c_high_cal))
        if len(high_cal) == 0:
            high_cal = c_high_cal
        low_cal = int(low_cal)
        high_cal = int(high_cal)
    filter_vars["m_low_cal"] = low_cal
    filter_vars["m_high_cal"] = high_cal
    
def get_calorie_options():
    return filter_vars["m_high_cal"], filter_vars["m_low_cal"]

def set_filter_counter():
    while True:
        number_returned = filter_vars["m_base_number_returned"]
        change_filter = input("The current option is to return {0} recipes in our search.\nWould you like to change that? (Default to No)\n".format(number_returned))
        if len(change_filter) == 0:
            change_filter = 'N'
        if change_filter.upper() == 'Y':
            number_returned = input("How many recipes should be shown? (Press Enter to keep at {0})".format(number_returned))
            if len(number_returned) == 0:
                number_returned = filter_vars["m_base_number_returned"]
            else:
                number_returned = int(number_returned)
                if number_returned < 1:
                    print("Any number less than 1 is invalid")
                    continue
                else:
                    break
    filter_vars["m_base_number_returned"] = number_returned
    
def get_filter_counter():
    return filter_vars["m_base_number_returned"]
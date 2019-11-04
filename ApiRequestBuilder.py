# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:06:51 2019

@author: ericp
"""

class ApiRequestBuilder:
    def __init__(self, main, hl):
        self.app_id = "ab4bf454"
        self.app_key = "80971399f1f660312ba74b72ad419237"
        
        health_items=["vegan","vegetarian","sugar-conscious","peanut-free","tree-nut-free","alcohol-free"]
        diet_items=["balanced","high-protein","low-fat","low-carb"]
        
        self.api_string = "https://api.edamam.com/search?q={main}&app_id={ai}&app_key={ak}&from=0&to=20&calories=591-722".format(main=main, ai=self.app_id, ak=self.app_key)
        if len(hl) > 0:
            for itm in hl:
                if itm in health_items:
                    self.api_string+="&health={hi}".format(hi=itm)
                elif itm in diet_items:
                    self.api_string+="&diet={di}".format(di=itm)
        
                
    def get_api_string(self):
        return self.api_string
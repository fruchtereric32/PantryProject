# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:06:51 2019

@author: ericp
"""
##The class ApiRequestBuilder is used to put together all the parts to get the API ready
class ApiRequestBuilder:
    ##The constructor takes in the main food being used, 
    ##the health list, calorie counters and filter number
    ##It then composes the api putting all teh variables in the right place
    def __init__(self, main, hl, lc, hc, fn):
        self.app_id = "ab4bf454"
        self.app_key = "80971399f1f660312ba74b72ad419237"
        
        health_items=["vegan","vegetarian","sugar-conscious","peanut-free","tree-nut-free","alcohol-free"]
        diet_items=["balanced","high-protein","low-fat","low-carb"]
        
        self.api_string = "https://api.edamam.com/search?q={main}&app_id={ai}&app_key={ak}&from=0&to={fn}&calories={l_c}-{h_c}".format(main=main, ai=self.app_id, ak=self.app_key, l_c=lc, h_c=hc, fn=fn)
        if len(hl) > 0:
            for itm in hl:
                if itm in health_items:
                    self.api_string+="&health={hi}".format(hi=itm)
                elif itm in diet_items:
                    self.api_string+="&diet={di}".format(di=itm)
        
    ##The function get_api_string takes the already built api string and returns it to be used            
    def get_api_string(self):
        return self.api_string
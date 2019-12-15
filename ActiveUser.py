class ActiveUser:
    def __init__(self,json_string):
        print(json_string)
        self.id = json_string[0][0]
        self.default_pantry = json_string[0][1]
        self.max_calories = json_string[0][2]
        self.min_calories = json_string[0][3]

    def get_high_cal(self):
        return self.max_calories

    def get_low_cal(self):
        return self.min_calories

    def get_user_id(self):
        return self.id

    def set_cal_levels(self,high,low):
        self.max_calories = high
        self.min_calories = low
class Heating():

    def __init__(self,name,current_temp,min_temp,max_temp):
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.__current_temp = current_temp

    @property
    def current_temp(self):
        return self.__current_temp
    
    @current_temp.setter
    def current_temp(self,value):
        if self.min_temp < value < self.max_temp:
            self.__current_temp = value
        elif self.min_temp > value:
            self.__current_temp = self.min_temp
        elif self.max_temp < value:
            self.__current_temp = self.max_temp

    def __str__(self):
        string = f"{self.name}: current temperature: {self.__current_temp}; allowed min: {self.min_temp}; allowed max: {self.max_temp}"
        return string
    
    def change_temperature(self,temp_change):
        self.current_temp += temp_change
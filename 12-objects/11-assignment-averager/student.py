class Averager():

    sum = 0
    number_of_values = 0

    def __init__(self):
        pass

    def add(self,value):
        self.sum += value
        self.number_of_values += 1

    def average(self):
        if self.number_of_values == 0:
            return 0
        return self.sum/self.number_of_values
    
    def reset(self):
        self.sum = 0
        self.number_of_values = 0



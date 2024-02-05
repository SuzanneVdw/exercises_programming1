class Averager:
    def __init__(self):
        self.reset()

    def reset(self):
        self.__sum = 0
        self.__count = 0

    def add(self, value):
        self.__sum += value
        self.__count += 1

    def average(self):
        return self.__sum / self.__count
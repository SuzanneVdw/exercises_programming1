class Unit():

    def __init__(self,health,firepower,armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor

    @property
    def health(self):
        return self.__health
    
    @property
    def firepower(self):
        return self.__firepower
    
    @property
    def armor(self):
        return self.__armor
    
    def shot_by(self,other):
        if other.firepower > self.armor:
            if other.firepower-self.armor > self.health:
                self.__health = 0
            else:
                self.__health = self.health - (other.firepower-self.armor)

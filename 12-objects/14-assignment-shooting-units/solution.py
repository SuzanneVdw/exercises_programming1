class Unit:
    def __init__(self, health, firepower, armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError()
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

    def shot_by(self, other):
        health_loss = max(0, other.firepower - self.armor)
        self.__health = max(0, self.__health - health_loss)
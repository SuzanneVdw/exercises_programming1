class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, string):
        return self.__password == string
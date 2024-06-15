class Tweet():

    def __init__(self,message,max_length):
        self.__message = message
        if max_length < 1:
            raise ValueError
        self.__max_length = max_length
        if len(self.__message) > self.max_length:
            self.message = self.message[0:self.max_length]
        

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self,string):
        if len(string) > self.max_length:
            self.message = string[0:self.max_length]
        else:
            self.__message = string

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self,number):
        if number < 1:
            raise ValueError
        self.__max_length = number
        if len(self.__message) > self.max_length:
            self.message = self.message[0:self.max_length]
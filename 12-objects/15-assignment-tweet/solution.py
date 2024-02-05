class Tweet:
    def __init__(self, message, max_length):
        self.__message = message  # Cannot call message setter, as it requires max_length to be initialized
        self.max_length = max_length

    def __truncate(self):
        self.__message = self.__message[:self.__max_length]

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message
        self.__truncate()

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, max_length):
        if max_length < 1:
            raise ValueError()
        self.__max_length = max_length
        self.__truncate()

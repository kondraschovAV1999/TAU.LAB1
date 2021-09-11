class CircuitBreaker:
    def __init__(self, name):
        self.name = name
        self.__state = False

    def turn_breaker_on(self):  # Метод для включения выключателя
        self.__state = True

    def turn_breaker_off(self):  # Метод для отключения выключателя
        self.__state = False

    def get_state(self):  # Метод для получения информации о положении выключателя
        return self.__state

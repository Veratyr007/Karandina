class Vehicle:
    __COLOR_VARIANTS = ["black", "purple", "red", "blue", "pink"]
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность: {self.__engine_power} л.с."

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color.lower()
            print(f"Цвет изменен на {self.__color}")
        else:
            print(f"Нельзя изменить цвет на {new_color}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_passengers_limit(self):
        return f"Лимит пассажиров: {self.__PASSENGERS_LIMIT}"



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.set_color('Green')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()

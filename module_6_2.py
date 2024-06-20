class Vehicle:
    def __init__(self, owner, model, engin_power, color):
        self.owner = owner  #владелец транспорта
        self.__model = model  #модель (марка) транспорта
        self.__engin_power = engin_power  #мощность двигателя
        self.__color = color  #название цвета

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engin_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец: ', self.owner)

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя поменять цвет на', new_color)


class Sedan(Vehicle):
    def car(self):
        print(self.__model)
        print(self.__engin_power)
        print(self.__color)




vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()

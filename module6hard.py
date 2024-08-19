
import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(colors1, int) and 0 <= colors1 <= 255 for colors1 in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)


    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            valid_sides = []
            for side in new_sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)

            self.__sides = valid_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides, filled=False):
        super().__init__(color, sides, filled=filled)
        self.__radius = sides / (2 * math.pi)

    def get_square(self):
        return self.__radius * 2 ** math.pi


class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, height, sides, filled=False):
        super().__init__(color, sides, filled=filled)
        self.__height = height

    def get_square(self):
        p = (self.__height / 2)
        sides = self.get_sides()
        return math.sqrt((p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])))


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides, filled=False):
        cube_sides = [sides] * 12
        super().__init__(color, cube_sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0][0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


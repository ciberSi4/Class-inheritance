# Дополнительное практическое задание по модулю: "Наследование классов."
import math

class Figure:
    sides_count = 0

    def __init__(self, color : tuple, sides : list):
        self.__sides : list = sides
        self.__color : list = list(color)
        self.color = []
        self.filled : bool = False
        self.sides : list = []
        self.new_sides : list = []

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        for i in range(len(self.color)):
            if 0 < self.color[i] > 255:
                self.filled = False
                break
            else:
                self.filled = True
        return self.filled

    def set_color(self, *color):
        self.color = color
        self.filled = self.__is_valid_color(self.color)
        if self.filled:
            self.__color = []
            for i in range(len(self.color)):
                self.__color.append(self.color[i])

    def __is_valid_sides(self, *new_sides):
        for i in range(len(self.new_sides)):
            if 0 < self.new_sides[i] or (len(self.new_sides) == self.sides_count):
                self.filled = True
            else:
                self.filled = False
                break
        return self.filled

    def get_sides(self):
        return self.sides

    def __len__(self):
        P = 0
        for i in range(len(self.sides)):
            P += self.sides[i]
        return P

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        self.filled = self.__is_valid_sides(self.new_sides)
        if self.filled:
            for i in range(0, len(self.new_sides)):
                self.sides.append(self.new_sides[i])
        return self.sides


class Circle(Figure):
    sides_count = 1

    def get_square(self):
        r = self._Figure__sides / (2 * math.pi)
        S = math.pi * r**2
        return S


class Triangle(Figure):
    sides_count = 3

    def get_square(self, a : int | float, b : int | float, c : int | float):
        p : int | float = 0
        p = (a + b + c) / 2
        S : int | float = math.sqrt(p * (p - a) * (p - b) * (p - c)) # Формула Герона
        return S


class Cube(Figure):
    sides_count = 12

    def get_sides(self):
        x = []
        y = self._Figure__sides
        for i in range(self.sides_count):
            x.append(y)
        self._Figure__sides = x
        return self._Figure__sides

    def get_volume(self):
        V = self._Figure__sides[0] ** 3
        return V

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
tr1 = Triangle((150, 150, 150), 15) # Дополнительные (свои проверки) работы методов объектов

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# tr1.set_color(175, 175, 175) # Изменится # Дополнительные (свои проверки) работы методов объектов
# print(tr1.get_color()) # Дополнительные (свои проверки) работы методов объектов
# tr1.set_color(175, 275, 175) # Не изменится # Дополнительные (свои проверки) работы методов объектов
# print(tr1.get_color()) # Дополнительные (свои проверки) работы методов объектов

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
# print(circle1.get_square()) # Дополнительные (свои проверки) работы методов объектов
# print(tr1.get_square(17, 8, 11)) # Дополнительные (свои проверки) работы методов объектов
print(cube1.get_volume())
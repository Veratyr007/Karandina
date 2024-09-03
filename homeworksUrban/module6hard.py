import math

class Figure:
    def __init__(self, color=(255, 255, 255), *sides):
        self._color = list(color) if self._is_valid_color(*color) else [255, 255,255]
        self.filled = False

        if len(sides) == self.sides_count:
            if self._is_valid_sides(*sides):
                self._sides = list(sides)
            else:
                self._sides = [1] * self.sides_count
        else:
            self._sides = [1] * self.sides_count


    def get_color(self):
        return self._color

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]
        else:
            print("Некорректные значения цвета, цвет остается прежним")

    def _is_valid_color(self, *colors):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in colors) and len(colors) == 3

    def _is_valid_sides(self, *sides):
        return all(isinstance(y, int) and y > 0 for y in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return tuple(self._sides)

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)
        else:
            print(f"Колличество сторон должно быть {self.sides_count}")

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(255, 255, 255), circumference=1):
        super().__init__(color, circumference)
        if len(self.get_sides()) == self.sides_count:
            self._radius = self._calculate_radius()
        else:
            print("У круга может быть только одна сторона - окружность")
            self._radius = 1

    def _calculate_radius(self):
        circumference = self.get_sides()[0]
        return circumference / (2 * math.pi)

    def get_area(self):
        return math.pi * (self._radius ** 2)

    def set_sides(self, circumference):
        super().set_sides(circumference)
        if len(self.get_sides()) == self.sides_count:
            self._radius = self._calculate_radius()
        else:
            print("У круга должна быть ровно одна сторона - окружность")

    def get_radius(self):
        return self._radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(255, 255, 255), a=1, b=1, c=1):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(255, 255, 255), edge_length=1):
        super().__init__(color, *(edge_length,) * self.sides_count)
        if len(self.get_sides()) == self.sides_count:
            self._edge_length = self.get_sides()[0]
        else:
            print("У куба должно быть 12 сторон")
            self._edge_length = 1

    def get_volume(self):
        return self._edge_length ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = new_sides * self.sides_count
        if len(new_sides) == self.sides_count and all(side == new_sides[0] for side in new_sides):
            super().set_sides(*new_sides)
            self._edge_length = self.get_sides()[0]
        else:
            print("У куба должно быть 12 равных сторон")

    def get_edge_length(self):
        return self._edge_length


            


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
























# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# A_x = int(input('введите координату X для вершины А'))
# A_y = int(input('введите координату Y для вершины А'))
# B_x = int(input('введите X координату для вершины B'))
# B_y = int(input('введите Y координату для вершины B'))
# C_x = int(input('введите X координату для вершины C'))
# C_y = int(input('введите Y координату для вершины C'))

import math


class triangle:
    def __init__(self, a, b, c):
        self._aX = int(a[0])
        self._aY = int(a[1])
        self._bX = int(b[0])
        self._bY = int(b[1])
        self._cX = int(c[0])
        self._cY = int(c[1])

    def side_length(self):
        self.ab = round(math.sqrt((self._bX - self._aX) ** 2 + (self._bY - self._aY) ** 2), 2)
        self.ac = round(math.sqrt((self._cX - self._aX) ** 2 + (self._cY - self._aY) ** 2), 2)
        self.bc = round(math.sqrt((self._cX - self._bX) ** 2 + (self._cY - self._bY) ** 2), 2)
        return self.ab, self.ac, self.bc

    def triangle_height(self):
        self.h = round(abs((self._bY - self._cY) * self._aX + (self._cX - self._bX) * self._aY + (
                self._bX * self._cY - self._cX * self._bY)) / math.sqrt(
            (self._bY - self._cY) ** 2 + (self._cX - self._bX) ** 2), 2)
        return self.h

    def perimeter(self):
        self.per = round(self.ab + self.ac + self.bc, 2)
        return self.per

    def triangle_area(self):
        self._s = round((self.bc * self.h) / 2, 2)
        return self._s


triangle = triangle([A_x, A_y], [B_x, B_y], [C_x, C_y])
print('Длина стороны АВ = {}, длина стороны AC = {}, длина стороны BC = {}'.format(triangle.side_length()[0],
                                                                                   triangle.side_length()[1],
                                                                                   triangle.side_length()[2]))
print('Высота треугольника из вершины А на сторону ВС = {}'.format(triangle.triangle_height()))
print('Периметр треугольника  = {}'.format(triangle.perimeter()))
print('Площадь треугольника = ', triangle.triangle_area())
#
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

A = (0, 2)
B = (0, 7)
C = (2, 5)
D = (2, 4)

import math


class trapezium:
    def __init__(self, a, b, c, d):
        self._aX = int(a[0])
        self._aY = int(a[1])
        self._bX = int(b[0])
        self._bY = int(b[1])
        self._cX = int(c[0])
        self._cY = int(c[1])
        self._dX = int(d[0])
        self._dY = int(d[1])

    def side_length(self):
        self.ab = round(math.sqrt((self._bX - self._aX) ** 2 + (self._bY - self._aY) ** 2), 2)
        self.ad = round(math.sqrt((self._dX - self._aX) ** 2 + (self._dY - self._aY) ** 2), 2)
        self.bc = round(math.sqrt((self._cX - self._bX) ** 2 + (self._cY - self._bY) ** 2), 2)
        self.cd = round(math.sqrt((self._dX - self._cX) ** 2 + (self._dY - self._cY) ** 2), 2)
        self.bd = round(math.sqrt((self._dX - self._bX) ** 2 + (self._dY - self._bY) ** 2), 2)
        self.ac = round(math.sqrt((self._cX - self._aX) ** 2 + (self._cY - self._aY) ** 2), 2)
        return self.ab, self.ad, self.bc, self.cd, self.bd, self.ac

    def if_trapezium(self):
        # трапеция равнобедренная, если диагонали равны
        return trapezium.side_length()[5] == trapezium.side_length()[4]

    def perimeter(self):
        self.per = round(self.ab + self.ac + self.bc + self.bd, 2)
        return self.per

    def area_trapezium(self):
        self._s = ((self.ad + self.bc) / 4) * math.sqrt(4 * (self.ab ** 2) - (self.ad - self.bc) ** 2)
        return self._s


trapezium = trapezium(A, B, C, D)

print('Траппеция равнобедренная = ', trapezium.if_trapezium())
print('Длины сторон: a = {}, b = {}, c = {}, d = {}'.format(trapezium.side_length()[0], trapezium.side_length()[1],
                                                            trapezium.side_length()[2], trapezium.side_length()[3]))
print('Периметр трапеции = ', trapezium.perimeter())
print('Площадь трапеции = ', trapezium.area_trapezium())

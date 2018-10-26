__author__ = 'Сащенко С.В.'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(n))
#
# Так и не смог разобраться как это работает

def fib_func(n, m):
    fib_list = [1, 1, ]
    el = 2
    while el < m:
        z = fib_list[el - 1] + fib_list[el - 2]
        fib_list.append(z)
        el += 1
    return fib_list[n:m]


n = int(input('Введите с какого члена последовательности Фибоначчи выводить ряд'))
m = int(input('Введите до какого члена последовательности выводить ряд'))
print(fib_func(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort(list):
    n = len(list)
    for j in range(0, n - 1):
        for i in range(0, n - j - 1):
            if list[i] >= list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


lst = [2, 5, 4, 2, 9, 8, 7, 6, 15, 0]
print(sort(lst))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def positive_number(list):
    new_list = []
    for i in list:
        if i >= 0:
            new_list.append(i)
    return new_list


lst = [-2, 5, 4, 2, -9, 8, -7, 6, 15, 0]
print(positive_number(lst))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math


def parallelogram(A, B, C, D):
    res = None
    # у паралеллограмма стороны попарно параллельны
    # проверим их длину
    AB = math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
    AC = math.sqrt((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2)
    AD = math.sqrt((D[0] - A[0]) ** 2 + (D[1] - A[1]) ** 2)
    BC = math.sqrt((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2)
    BD = math.sqrt((D[0] - B[0]) ** 2 + (D[1] - B[1]) ** 2)
    CD = math.sqrt((D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2)
    # условие: как минимум должно быть 2 пары одинаковых значений
    # создадим список с полученными значениями
    result = [AB, AC, AD, BC, BD, CD]
    res_list = []
    for i in result:
        if result.count(i) == 2:
            res_list.append('ok')
        if result.count(i) == 4:
            res = True
            break
        else:
            res = False
    if len(res_list) >= 4:
        res = True
    else:
        res = False
    return (res)


A_x = int(input('введите координат X первой точки'))
A_y = int(input('введите координаты Y первой точки'))
B_x = int(input('введите  координаты X второй точки'))
B_y = int(input('введите Y координаты второй точки'))
C_x = int(input('введите X координаты третьей точки'))
C_y = int(input('введите Y  координаты третьей точки'))
D_x = int(input('введите X координаты червертой точки'))
D_y = int(input('введите Y координаты червертой точки'))
A = (A_x, A_y)
B = (B_x, B_y)
C = (C_x, C_y)
D = (D_x, D_y)

print(parallelogram(A, B, C, D))

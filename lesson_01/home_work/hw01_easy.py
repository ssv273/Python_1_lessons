__author__ = 'Сащенко С.В.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).

# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = int(input("Введите произвольное число: "))
i = number
while i:
    ost = i % 10
    i = i // 10
    print(ost)
print("Конец.")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
number_1 = input("Введите значение №1:")
number_2 = input("Введите значение №2:")
f=number_1
g=number_2
number_1=g
number_2=f
print("Теперь значение №1 стало: ",number_1)
print("Теперь значение №2 стало: ",number_2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input("Введите Ваш возраст:"))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
__author__ = 'Сащенко С.В.'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# ПОКА РАБОТАЕТ ТОЛЬКО С ПОЛОЖИТЕЛЬНЫМИ ЧИСЛАМИ, потом допилю чтобы работало с любыми

expression = '5/6 + 4/7'

# ищем первое вхождение пробела и запоминаем его
gap_1 = int(expression.find(' '))
# ищем первое вхождение знака дроби и запоминаем его
fraction_1 = expression.find('/')
# определяем переменную для целого в дроби №1
whole_part_1 = None
# Определяем переменную для числителя №1
numerator_1 = None
# определяем переменную для знаменателя №1
denominator_1 = None
# если первое вхождение дроби ранее чем пробела то определяем числитель и знаменатель первой дроби
if gap_1 > fraction_1:
    numerator_1 = int(expression[:fraction_1])
else:
    whole_part_1 = int(expression[:gap_1])

if gap_1 < fraction_1:
    numerator_1 = int(expression[gap_1:fraction_1])
    whole_part_1 = int(expression[:gap_1])
# нашли целую часть и числитель, находим знаменатель. находим знак арифметического действия
arithmetic_operation_summ = int(expression.find('+'))
arithmetic_operation_subtraction = int(expression.find('-'))
if arithmetic_operation_summ != -1:
    denominator_1 = int(expression[fraction_1 + 1:arithmetic_operation_summ])
else:
    denominator_1 = int(expression[fraction_1 + 1:arithmetic_operation_subtraction])
print('Целая честь первой дроби = ', whole_part_1)
print('Числитель первой дроби = ', numerator_1)
print('Знаменатель первой дроби = ', denominator_1)

# определяем переменную для целого в дроби №2
whole_part_2 = None
# Определяем переменную для числителя №2
numerator_2 = None
# определяем переменную для знаменателя №2
denominator_2 = None
# ищем последнее вхождение дроби
fraction_2 = expression.rfind('/')
# все что после знака дроби это знаменатель
denominator_2 = int(expression[fraction_2 + 1:])
# ищем последнее вхождение пробела, все что от него до знака дроби это числитель
gap_2 = int(expression.rfind(' '))
# print(gap_2)
numerator_2 = int(expression[gap_2:fraction_2])
# теперь все что после арифметического знака и до пробела это целое число дроби №2, усли оно есть
# ищем пробел после знака действия, если он есть значит есть целая часть
gap_3 = 0
gap_4 = 0
if arithmetic_operation_summ > 1:
    gap_3 = int(expression.find(' ', arithmetic_operation_summ + 2, len(expression)))
else:
    gap_4 = int(expression.find(' ', arithmetic_operation_subtraction + 2, len(expression)))
# print('вхождение знака арифметического действия = ', arithmetic_operation_summ)
# print('вхождение пробела после знака арифметического действия сумма = ', gap_3)
# print('вхождение пробела после знака арифметического действия разность = ', gap_4)
if gap_3 > 0 or gap_4 > 0:
    if gap_3 > gap_4:
        whole_part_2 = int(expression[arithmetic_operation_summ + 1:gap_2])
    else:
        whole_part_2 = int(expression[arithmetic_operation_subtraction + 1:gap_2])
print('Целая часть второй дроби = ', whole_part_2)
print('Числитель второй дроби = ', numerator_2)
print('Знаменатель второй дроби = ', denominator_2)

# проверяем на наличие целой части, если ее нет, то ставим равной 1
if whole_part_1 == None:
    whole_part_1 = 1
if whole_part_2 == None:
    whole_part_2 = 1

# приводим дробь к неправильному виду
if whole_part_1 > 1:
    numerator_1 = numerator_1 + denominator_1 * whole_part_1
    # print(numerator_1, '/', denominator_1)
if whole_part_2 > 1:
    numerator_2 = numerator_2 + denominator_2 * whole_part_2
    # print(numerator_2, '/', denominator_2)
# приводим дробь к общему знаменателю
numerator_1 = numerator_1 * denominator_2
numerator_2 = numerator_2 * denominator_1
denominator_1, denominator_2 = denominator_1 * denominator_2, denominator_1 * denominator_2
# определяем знак арифметического действия и производим его
if arithmetic_operation_summ > 0:
    res_numenator = numerator_1 + numerator_2
if arithmetic_operation_subtraction > 0:
    res_numenator = numerator_1 - numerator_2
# выделяем целую часть
if (res_numenator // denominator_1) > 0:
    res_whole_part = res_numenator // denominator_1
    res_numenator = res_numenator - res_whole_part * denominator_1
# упрощаем дробь
# находим НОД
a = res_numenator
b = denominator_1
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
nod = a + b
# ну и наконец выводим результат
print('Ответ = {} {}/{}'.format(res_whole_part, int(res_numenator / nod), int(denominator_1 / nod)))
# фууух...


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


import os

path_zp = os.path.join('data', 'workers')

# считываем в список значения из файла
with open(path_zp, 'r', encoding='UTF-8') as f:
    onstring = f.read().split('\n')[:-1]
print(onstring[])
head_str = str(onstring[0])
print(head_str, type(head_str))
head_list = head_str.split( )
print(head_list)
# вобщем идея в том чтобы создать список с фамилиями, список с окладом, с нормочасами и отработаными часами, и потом их
# обрабатывать. Времени не хватило.


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


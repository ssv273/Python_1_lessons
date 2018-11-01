# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import Scripts.easy as easy

answer = ''
while answer != "q":
    answer = input("Поработаем? (y/n/q)")
    if answer == "y":
        print(" [1] - Перейти в папку")
        print(" [2] - Просмотреть содержимое текущей папки")
        print(" [3] - Удалить папку")
        print(" [4] -Создать папку")
        do = int(input("Укажите номер действия: "))
        if do == 1:
            easy.change_dir()
        elif do == 2:
            easy.view_dir()
        elif do == 3:
            easy.del_dir()
        elif do == 4:
            easy.make_dir()
        else:
            pass
    elif answer == "n":
        print("До свидания!")
        break
    else:
        print("Неизвестный ответ")

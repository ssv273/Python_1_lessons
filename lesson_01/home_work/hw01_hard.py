__author__ = 'Сащенко С.В.'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)


# Ход моих рассуждений:
# Сначала собрал такой код - 
# a = 0
# a = int(a)
# f = 0
# while f != 3:
    # if a == a**2 and a == a * 2 and a > 999999:
        # f=3
        # break
    # print(f)
    # print(a)
    # a+=1

# И понял что он будет работать бесконечно, т.к. а=а*2 будет верно только при одном случае,когда а=0
# запустил, посмотрел как изменяется а, и загрустил. И смотреть мне на него до седых волос и дальше, бесконечно...
# Бесконечно? Эврика, значение а=бесконечность. Ну а дальше гугл "как присвоить значение "бесконечность".
# И вот что получается
import math

a = math.inf        # Присвоили переменной a значение "бесконечность"
if a == a**2 and a == a * 2 and a > 999999:
	print("a = бесконечность")
else:
	print("Тогда я не в курсе")
# ух, работает

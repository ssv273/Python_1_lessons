# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import random
import string
import re

def condition(list):
    # Проверяем условие, все ли символы вокруг символов в верхнем регистре
    if len(list)==1:
        res = 'Нет таких символов.'
    else:
        res = list
    return res

# С тспользованием RE
str_1 = 'KQKAtsaxpR'
# str_1 = str_1.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10)])
print('Исходная строка: ', str_1)
pattern = '([a-z]+)[A-Z]+'
res = re.findall(pattern, str_1)
print(condition(res))

# 1-е Решение без использования RE
str_1 = 'mtMmEZUOmcq'
print('Исходная строка: ', str_1)

lst_1 = list(str_1)
new_lst_lower = []
count_lower = 0
for i in str_1:
    if i.islower():
        new_lst_lower.append(str_1.index(i, count_lower))
        count_lower = str_1.index(i, count_lower) + 1
res_str = ''
a = 0
ind = 0
while a < (max(new_lst_lower) + 1):
    if a == new_lst_lower[ind]:
        res_str += str_1[new_lst_lower[ind]]
        ind += 1
    else:
        res_str += ' '
    a += 1
res_lst = res_str.split()
print(condition(res_lst))

# 2-е Решение без использования RE
str_1 = 'mtMmEZUOmcq'
for i in str_1:
    if i.isupper():
        str_1 = str_1.replace(i, ' ')
res_lst = str_1.split()
print(condition(res_lst))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.


import random
import string
import re

str_2 = ''
str_1 = str_2.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(80)])
print('Исходная строка: ', str_1)
res = re.findall("[a-z]{2}([A-Z]+)[A-Z]{2}", str_1)
print(res)




# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random
import re
with open("data/num.txt", "w", encoding='UTF-8') as f:
    f.write("".join(str(random.randint(0, 9)) for _ in range(2500)))
with open("data/num.txt", "r", encoding='UTF-8') as f:
    data = f.read()
pattern = re.compile('(1+)|(2+)|(3+)|(4+)|(5+)|(6+)|(7+)|(8+)|(9+)|(0+)')
lst = re.findall(pattern, data)
flat_list = [item for sublist in lst for item in sublist if item != ""]
max_len_seq = str(max(list(map(int, flat_list))))
print(f"Самая длинная последовательность одинаковых цифр в вышезаполненном файле: {max_len_seq}")
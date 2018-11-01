# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

try:
    a = 1
    while a < 10:
        path = 'dir_' + str(a)
        os.mkdir(path)
        a += 1
except OSError:
    print('Такая директория уже существует.')

try:
    b = 1
    while b < 10:
        path = 'dir_' + str(b)
        os.rmdir(path)
        b += 1
except OSError:
    print('Директорий с тaким именем не найдено.')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
path = os.getcwd()
for root, dirs, files in os.walk(path):
    print(root)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys

# print(sys.argv)
path = ''.join(sys.argv)
file = os.path.basename(path)
print(file)
file_copy = file[:len(file)-3]+'_copy'+ file[len(file)-3:]
print(file_copy)
shutil.copy(file, file_copy)
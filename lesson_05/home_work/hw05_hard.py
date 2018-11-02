# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('cd <dir_name> - меняет текущую директорию на одну из внутренних')
    print('ls - отображение полного пути текущей директории')


def rm():
    print("Удаление указанного файла")
    key = ''
    while True:
        filename = os.path.join(input("Укажите имя файла: "))
        key = input('Вы действительно хотите удалить этот файл (y/n)')
        if key == 'y':
            os.remove(filename)
            print('Файл ', filename, ' успешно удален')

        else:
            print('skfjvbaksjfv')
            sys.exit()

def cd():
    dir_name = input('Введите имя диретории в которую Вы хотите перейти, или ".." для перехода на уровеньвыше')
    full_pafh = os.path.join(dir_name)
    os.chdir(full_pafh)
    print(sys.argv)


def ls():
    print(os.getcwd())

def cp():
    import shutil
    print("Дублирование пользовательского файла")
    filename = input("Укажите имя файла: ")
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        print('Копия файла ', filename, ' создана')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

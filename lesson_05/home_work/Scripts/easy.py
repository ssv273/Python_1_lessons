# [1] - Перейти в папку")

def change_dir():
    import  os
    path = input('Введите путь к новой директории:')
    os.chdir(path)
    print('Перешел в директорию: ', os.getcwd())


#" [2] - Просмотреть содержимое текущей папки"

def view_dir():
    import os



    path = os.getcwd()
    print(os.listdir(path))

    # for root, dirs, files in os.walk(path):
    #     print(root)
    #     print(dirs)
    #     print(files)


 # [3] - Удалить папку

def del_dir():
    import os
    path = input('Введите путь к папке, которую необходимо удалить: ')
    os.rmdir(path)
    print('Папка удалена.')


# [4] -Создать папку
def make_dir():
    import os
    path = input('Введите путь к папке, которую необходимо создать: ')
    os.mkdir(path)
    print('Папка успешно создана.')


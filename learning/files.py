import os
import os.path
import shutil
import json

'''Текущая директория'''
cur = os.getcwd()
print(cur)

'''Указать новую текущую директорию'''
# os.chdir("c:\\Python34")

'''Получить список файлов в директории'''
# os.listdir("c:\\Python34")
'''Текущая директория'''
cur2 = os.listdir(".")
print(cur2)
'''Файлы в папке из текущей директории'''
# os.listdir("Scripts")

'''Path'''
'''Это файл? = True'''
os.path.isfile("files.py")
'''Это папка?'''
os.path.isdir("Scripts")
'''Фильтруем, оставляя только файлы'''
spisok_failov = list(filter(lambda f: os.path.isfile(f), os.listdir(".")))
print(spisok_failov)

'''Создание, удаление, копирование
Создаётся пустая папка в текущей'''
# os.mkdir("test")
'''Создаются пустые вложенные папки'''
# os.makedirs("test1\\test2\\test3")
'''Удаляет указанную папку'''
# os.rmdir("test")
'''удаляет файл'''
# os.remove("c:\\Python34\\README.txt")

'''Удаляет папку вместе с её содержимым (и вложенными папками)'''
# shutil.rmtree("test1")
'''копировать что и куда'''
# shutil.copy("c:/Python34/README.txt", "c:/temp/py")

'''Чтение, запись файла'''
f1 = open("lists.py")
text = f1.read()
print(text)
f1.close()

'''требуем записать в файл'''
# f2 = open("c:/Python34/README.txt", "w")
# f2.write(text)
'''Окончательная запись в файл происходит во время закрытия файла'''
# f2.close()

'''JSON + try'''
f = open("config.json")
try:
    res = json.load(f)
except ValueError as ex:
    '''Перехват ошибки'''
    print(ex)
    res = {}
finally:
    '''выполнится в любом случае'''
    f.close()

''' "Возвращает" словарь '''
print(res)
print(res["browser"]["type"])

'''Файл будет использоваться только в рамках блока и закроется сам'''
with open("config.json") as f3:
    try:
        res2 = json.load(f3)
    except ValueError as ex:
        print(ex)
        res2 = {}


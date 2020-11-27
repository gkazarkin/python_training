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
cur2 = os.listdir(".")  # Текущая директория
print(cur2)
# os.listdir("Scripts")  # Файлы в папке из текущей директории

'''Path'''
os.path.isfile("files.py")  # Это файл? = True
os.path.isdir("Scripts")  # Это папка?
# Фильтруем, оставляя только файлы
spisok_failov = list(filter(lambda f: os.path.isfile(f), os.listdir(".")))
print(spisok_failov)

'''Создание, удаление, копирование'''
# os.mkdir("test")  # Создаётся пустая папка в текущей
# os.makedirs("test1\\test2\\test3")  # Создаются пустые вложенные папки
# os.rmdir("test")  # Удаляет указанную папку
# os.remove("c:\\Python34\\README.txt")  # удаляет файл

# shutil.rmtree("test1")  # Удаляет папку вместе с её содержимым (и вложенными папками)
# shutil.copy("c:/Python34/README.txt", "c:/temp/py")  # копировать что и куда

'''Чтение, запись файла'''
f1 = open("lists.py")
text = f1.read()
print(text)
f1.close()

# f2 = open("c:/Python34/README.txt", "w")  # требуем записать в файл
# f2.write(text)
# f2.close()  # Окончательная запись в файл происходит во время закрытия файла

'''JSON + try'''
f = open("config.json")
try:
    res = json.load(f)
except ValueError as ex:  # Перехват ошибки
    print(ex)
    res = {}
finally:  # выполнится в любом случае
    f.close()

print(res)  # Возвращает словарь
print(res["browser"]["type"])

with open("config.json") as f3:  # Файл будет использоваться только в рамках блока и закроется сам
    try:
        res2 = json.load(f3)
    except ValueError as ex:  # Перехват ошибки
        print(ex)
        res2 = {}


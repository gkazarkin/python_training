from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

"""getopt- чтение опций командной строки, n- количество генерируемых данных, f- файл, куда записывать"""
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

"""Перебор в котором рассматривается что ввели в командную строку и преобразуется в параметры
-n 10 -f data/groupdata.json """
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

"""Генератор групп"""
def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits  # Генерируем символы

    '''Выбирает символы и склеивает этот список без пробелов через join в строку'''
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


'''Баг: аппостроф ' в header или +20 символов не позволит создать группу
Словарь. Генерит с префиксом (name) + не более 10 символов
list comprehension, цикл 5 раз '''
testdata = [
        Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
        for name in range(n)
]

'''1- выясняем абсолютный путь до проекта и подклеиваем к нему подняться на 1 уровень вверх и нужный путь'''
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

"""Открывает файл с записью данных.
json- Сначала объект превращаем в словарь, потом через dumps в строку в формате json
jsonpickle- сериализация объект Group"""
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))  # Через jsonpickle
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))  # Через json

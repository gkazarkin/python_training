from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import random
import string
import os.path
import jsonpickle
import getopt
import sys

"""getopt- чтение опций командной строки, n- количество генерируемых данных, f- файл, куда записывать"""
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

"""Перебор в котором рассматривается что ввели в командную строку и преобразуется в параметры
-n 10 -f data/contactdata.json """
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

"""Генератор контактов"""
def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits  # Генерируем символы

    '''Выбирает символы и склеивает этот список без пробелов через join в строку'''
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    gen_digits = str(string.digits)
    return "".join([random.choice(gen_digits) for i in range(random.randrange(maxlen))])

def random_symbols(maxlen):
    gen_symbols = string.ascii_letters + str(string.digits)
    # return prefix + "".join([random.choice(gen_symbols) for i in range(random.randrange(maxlen))])
    return "".join([random.choice(gen_symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    gen_email = string.ascii_letters + str(string.digits)
    return ("".join([random.choice(gen_email) for i in range(random.randrange(maxlen))])) + "@" +\
           ("".join([random.choice(gen_email) for i in range(random.randrange(maxlen))])) + ".ru"


'''Баг: аппостроф ' в header или +20 символов не позволит создать группу
Словарь. Генерит с префиксом (name) + не более 10 символов
list comprehension, цикл 5 раз '''
testdata = [
        Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                nickname=random_symbols(10), title=random_symbols(10), company=random_symbols(10),
                address=random_symbols(10), homephone=random_digits(6), mobilephone=random_digits(11),
                workphone=random_digits(6), fax=random_digits(6), email=random_email(7),  email2=random_email(7),  email3=random_email(7),
                homepage=random_email(8), bday="11", bmonth="April", byear="1987", aday="11", amonth="April", ayear="1987",
                address2=random_symbols(10), secondaryphone=random_digits(11), notes=random_symbols(10))
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

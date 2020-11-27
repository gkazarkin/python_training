from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10  # Генерируем символы

    '''Выбирает символы и склеивает этот список без пробелов через join в строку'''
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


'''Баг: аппостроф ' в header или +20 символов не позволит создать группу
Словарь. Генерит с префиксом (name) + не более 10 символов
list comprehension, цикл 5 раз '''
testdata = [
        Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
        for name in range(3)
]

# testdata = [Group(name="", header="", footer="")] + [
#         Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
#         for name in range(3)
# ]



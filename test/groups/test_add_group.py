# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string

def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10  # Генерируем символы
    # Выбирает символы и склеивает этот список без пробелов через join в строку
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Баг: аппостроф ' в header или +20 символов не позволит создать группу
testdata = [Group(name="", header="", footer="")] + [  # Список
        # Генерит с префиксом (name) + не более 10 символов
        Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
        for name in range(3)  # list comprehension, цикл 5 раз

        # Group(name=name, header=header, footer=footer)
        # for name in ["", random_string("name", 10)]  # list comprehension, пробегает по 2 возможным значениям
        # for header in ["", random_string("header", 20)]
        # for footer in ["", random_string("footer", 20)]
    ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])  # Передаёт параметры и какие именно
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
    new_groups = app.group.get_group_list()

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)






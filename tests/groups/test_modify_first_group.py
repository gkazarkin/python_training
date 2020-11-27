# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    '''Генерируем случайное число от 0 до количества групп'''
    index = randrange(len(old_groups))
    group = Group(name="Modif_group")
    group.id = old_groups[index].id  # Запоминаем id
    app.group.modify_group_by_index(index, group)

    '''Выступает в роли хеширования количества групп'''
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    '''Генерируем случайное число от 0 до количества групп'''
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    '''Выступает в роли хеширования количества групп'''
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()

    old_groups[index:index+1] = []
    assert old_groups == new_groups




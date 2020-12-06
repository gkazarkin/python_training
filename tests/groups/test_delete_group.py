# -*- coding: utf-8 -*-
import pytest
from model.group import Group
# from random import randrange
import random

"""Список групп берётся из базы данных"""
def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)

    app.group.delete_group_by_id(group.id)
    '''Выступает в роли хеширования количества групп'''
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = db.get_group_list()

    old_groups.remove(group)
    assert old_groups == new_groups
    """Опциональный флаг проверки через UI
    Прописать запуск можно или в консоли или справа вверху Edit_Configuration - Additional arguments (Options) --check_ui"""
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



"""Список групп берётся из UI"""
# def test_delete_some_group(app):
#     if app.group.count_groups() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     '''Генерируем случайное число от 0 до количества групп'''
#     index = randrange(len(old_groups))
#     app.group.delete_group_by_index(index)
#     '''Выступает в роли хеширования количества групп'''
#     assert len(old_groups) - 1 == app.group.count_groups()
#     new_groups = app.group.get_group_list()
#
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups




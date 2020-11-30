# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_add_group(app, json_groups):
    old_groups = app.group.get_group_list()
    app.group.create(json_groups)

    """Выступает в роли хеширования количества групп"""
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()

    old_groups.append(json_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""Название параметра указывает на источник данных"""
# def test_add_group(app, data_groups):
#     # group = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(data_groups)
#
#     assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
#     new_groups = app.group.get_group_list()
#
#     old_groups.append(data_groups)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""Параметризация из сгенерированных данных в groups"""
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])  # Передаёт параметры и какие именно
# def test_add_group(app, group):
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#
#     assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
#     new_groups = app.group.get_group_list()
#
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)






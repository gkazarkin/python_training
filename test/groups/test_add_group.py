# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test_group", header="test1", footer="test2")
    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
    new_groups = app.group.get_group_list()

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#
#     old_groups.append(group)  # sortirovka i sravnenie spiska groups
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





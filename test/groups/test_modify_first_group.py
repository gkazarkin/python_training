# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    group = Group(name="Modif_group")
    group.id = old_groups[0].id  # zapominaem id

    app.group.modify_first_group(group)

    assert len(old_groups) == app.group.count_groups()  # Выступает в роли хеширования количества групп
    new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




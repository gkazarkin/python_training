# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import testdata
# from data.add_group import constant as testdata
import random
import string

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])  # Передаёт параметры и какие именно
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
    new_groups = app.group.get_group_list()

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)






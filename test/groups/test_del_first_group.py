# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()

    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)  # sravnenie razmerov group

    old_groups[0:1] = []  # virezat perviy element pod indexom 0
    assert old_groups == new_groups




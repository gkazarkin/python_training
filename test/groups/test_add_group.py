# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="test_group", header="test1", footer="test2"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))




# -*- coding: utf-8 -*-
import pytest
from model.groupredata import GroupRedata

def test_add_group(app):
    app.group.create(GroupRedata(name="test_group", header="test1", footer="test2"))

def test_add_empty_group(app):
    app.group.create(GroupRedata(name="", header="", footer=""))




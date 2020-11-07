# -*- coding: utf-8 -*-
import pytest
from model.groupredata import GroupRedata

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(GroupRedata(name="test_group", header="test1", footer="test2"))
    app.session.log_out()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(GroupRedata(name="", header="", footer=""))
    app.session.log_out()



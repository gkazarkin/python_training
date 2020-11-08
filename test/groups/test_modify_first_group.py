# -*- coding: utf-8 -*-
import pytest
from model.groupredata import GroupRedata

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(GroupRedata(name="New group"))
    app.session.log_out()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(GroupRedata(header="New header"))
    app.session.log_out()

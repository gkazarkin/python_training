# -*- coding: utf-8 -*-
import pytest
from model.groupredata import GroupRedata

def test_modify_group_name(app):
    app.group.modify_first_group(GroupRedata(name="New group"))

def test_modify_group_header(app):
    app.group.modify_first_group(GroupRedata(header="New header"))

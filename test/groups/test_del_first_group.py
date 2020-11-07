# -*- coding: utf-8 -*-
import pytest
from model.groupredata import GroupRedata

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.log_out()
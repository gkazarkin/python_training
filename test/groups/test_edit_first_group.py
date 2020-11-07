# -*- coding: utf-8 -*-
import pytest

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.session.log_out()

# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

# inicializator fixtyri
@pytest.fixture()
def app(request):
    fixture = Application()
    # ykazanie na to, kak razrushit fixtyry
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="test_group", header="test1", footer="test2"))
    app.session.log_out()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.log_out()



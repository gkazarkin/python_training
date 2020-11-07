# -*- coding: utf-8 -*-
from model.acc import Acc
from fixture.application import Application
import pytest
from fixture.crt_acc import AccHelper

# inicializator fixtyri
@pytest.fixture()
def app(request):
    fixture = Application()
    # ykazanie na to, kak razrushit fixtyry
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_acc(app):
    app.session.login(username="admin", password="secret")
    app.crt_acc.add_new_acc(
        Acc(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle", company="TestCompany",
            address="Yakovleva 5", home="515232", mobile="89539235812", work="367412", fax="89539234611", email="gkazarkin@test.ru",
            email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11", amonth="April",
            ayear="1987", phone2="515232", adress2="Yakovleva 5", notes="Test Note"))
    app.crt_acc.check_add_acc()
    app.session.log_out()

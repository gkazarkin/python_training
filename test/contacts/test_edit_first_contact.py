from model.contactsredata import ContactsRedata
import pytest
from fixture.contact import ContactHelper

def test_add_acc(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        ContactsRedata(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                       company="TestCompany",
                       address="Yakovleva 5", home="515232", mobile="89539235812", work="367412", fax="89539234611",
                       email="gkazarkin@test.ru",
                       email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                       amonth="April",
                       ayear="1987", phone2="515232", adress2="Yakovleva 5", notes="Test Note"))
    app.session.log_out()

from model.contact import Contact
import pytest
from fixture.contact import ContactHelper

def test_modify_title(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany",
                    address="Yakovleva 5", home="515232", mobile="89539235812", work="367412", fax="89539234611",
                    email="gkazarkin@test.ru",
                    email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April",
                    ayear="1987", address2="Yakovleva 5", phone2="515232", notes="Test Note"))
    app.contact.modify_first_contact(Contact(title="ContactTitle"))

def test_modify_home_number(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany",
                    address="Yakovleva 5", home="515232", mobile="89539235812", work="367412", fax="89539234611",
                    email="gkazarkin@test.ru",
                    email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April",
                    ayear="1987", address2="Yakovleva 5", phone2="515232", notes="Test Note"))
    app.contact.modify_first_contact(Contact(home="415212"))

# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                      company="TestCompany", address="Yakovleva 5", home="515232", mobile="89539235812", work="367412",
                      fax="89539234611", email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com",
                      bday="11", bmonth="April", byear="1987", aday="11", amonth="April", ayear="1987", address2="Yakovleva 5",
                      phone2="515232", notes="Test Note")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    app.contact.check_added_contact()

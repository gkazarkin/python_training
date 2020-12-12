# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import random
import string
from data.contacts import contact_testdata
from model.group import Group
from model.contact import Contact

def test_add_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany", address="Yakovleva 5",
                    homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
                    email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()

    random_group = random.choice(old_groups)
    random_contact = random.choice(old_contacts)
    app.contact.add_to_group(contact_id=random_contact.id, group_id=random_group.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

    """Опциональный флаг проверки через UI
            Прописать запуск можно или в консоли или справа вверху Edit_Configuration - Additional arguments (Options) --check_ui"""
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

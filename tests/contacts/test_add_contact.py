# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import random
import string
from data.contacts import contact_testdata

def test_add_contact(app, json_contacts):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(json_contacts)

    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# '''Передаёт параметры и какие именно'''
# @pytest.mark.parametrize("contact", contact_testdata, ids=[repr(x) for x in contact_testdata])
# def test_add_contact(app, contact):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.add_new_contact(contact)
#
#     # assert len(old_contacts) + 1 == app.contact.count_contacts()  # Hash
#     # new_contacts = app.contact.get_contact_list()
#
#     assert len(old_contacts) + 1 == app.contact.count_contacts()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

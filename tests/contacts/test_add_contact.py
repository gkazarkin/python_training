# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import random
import string

def random_string(prefix, maxlen):
    gen_string = string.ascii_letters + " "  # Генерируем символы
    # Выбирает символы и склеивает этот список без пробелов через join в строку
    return prefix + "".join([random.choice(gen_string) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    gen_digits = string.digits + " "
    return "".join([random.choice(gen_digits) for i in range(random.randrange(maxlen))])

def random_symbols(prefix, maxlen):
    gen_symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(gen_symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    gen_email = string.ascii_letters + string.digits
    return ("".join([random.choice(gen_email) for i in range(random.randrange(maxlen))])) + "@" +\
           ("".join([random.choice(gen_email) for i in range(random.randrange(maxlen))])) + ".ru"


testdata = [
        Contact(firstname=random_string("F", 10), middlename=random_string("Jr. ", 10), lastname=random_string("L", 10),
                nickname=random_symbols("Nick", 10), title=random_symbols("Title", 10), company=random_symbols("Company", 10),
                address=random_symbols("Moscow ", 10), homephone=random_digits(6), mobilephone=random_digits(11),
                workphone=random_digits(6), fax=random_digits(6), email=random_email(7),  email2=random_email(7),  email3=random_email(7),
                homepage=random_email(8), bday="11", bmonth="April", byear="1987", aday="11", amonth="April", ayear="1987",
                address2=random_symbols("Lenina ", 10), secondaryphone=random_digits(11), notes=random_symbols("Notes ", 10))
        for name in range(2)  # list comprehension, цикл 5 раз
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])  # Передаёт параметры и какие именно
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(contact)

    # assert len(old_contacts) + 1 == app.contact.count_contacts()  # Hash
    # new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
from random import randrange

def test_modify_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="testNickName", title="AccTitle",
                    company="TestCompany", address="Yakovleva 5",
                    homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
                    email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April",
                    byear="1987", aday="11", amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))

    old_contacts = app.contact.get_contact_list()
    '''Генерируем случайный индекс от 0 до количества контактов'''
    index = randrange(len(old_contacts))
    print(index)
    contact = Contact(firstname="Modif_firstname", lastname="Modif_lastname")
    contact.id = old_contacts[index].id  # Запоминаем id

    app.contact.modify_contact_by_index(index, contact)

    # assert len(old_contacts) == app.contact.count_contacts()  #Hash
    # new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

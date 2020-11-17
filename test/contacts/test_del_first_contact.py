from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany",
                    address="Yakovleva 5", home="515232", mobile="89539235812", work="367412", fax="89539234611",
                    email="gkazarkin@test.ru",
                    email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April",
                    ayear="1987", address2="Yakovleva 5", phone2="515232", notes="Test Note"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))  # Генерируем случайный индекс от 0 до количества контактов
    app.contact.delete_contact_by_index(index)

    # assert len(old_contacts) - 1 == app.contact.count_contacts()  #Hash
    # new_contacts = app.contact.get_contact_list()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count_contacts()  # sravnenie razmerov group

    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

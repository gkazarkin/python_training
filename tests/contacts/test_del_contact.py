from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
# from random import randrange
import random

"""Сравнение списка из базы данных"""
def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany", address="Yakovleva 5",
                    homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
                    email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))

    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count_contacts()

    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

    """Опциональный флаг проверки через UI
            Прописать запуск можно или в консоли или справа вверху Edit_Configuration - Additional arguments (Options) --check_ui"""
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


"""Сравнение списка в UI"""
# def test_delete_first_contact(app):
#     if app.contact.count_contacts() == 0:
#         app.contact.add_new_contact(
#             Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
#                     company="TestCompany", address="Yakovleva 5",
#                     homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
#                     email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
#                     amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))
#
#     old_contacts = app.contact.get_contact_list()
#     '''Генерируем случайный индекс от 0 до количества контактов'''
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#
#     # assert len(old_contacts) - 1 == app.contact.count_contacts()  # Hash
#     # new_contacts = app.contact.get_contact_list()
#     new_contacts = app.contact.get_contact_list()
#     '''Сравнение размеров списков'''
#     assert len(old_contacts) - 1 == app.contact.count_contacts()
#
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts

from fixture.contact_methods import ContactHelper
import random
import string
from data.contacts import contact_testdata
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture

"""Ещё не доделан"""
def test_del_from_group(app, db, check_ui):
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

    try:
        db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
        l = db.get_contacts_in_group(Group(id="330"))
        for item in l:
            print(item)
        assert (len(l)) > 0
        print(len(l))
    finally:
        pass

    """Указывается ID группы"""
    # app.contact.del_from_group(group_id=random_group.id)
    app.contact.del_from_group(group_id=330)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

    """Опциональный флаг проверки через UI
            Прописать запуск можно или в консоли или справа вверху Edit_Configuration - Additional arguments (Options) --check_ui"""
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
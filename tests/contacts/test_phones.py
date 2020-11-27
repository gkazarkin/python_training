from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import re

def test_phones_on_home_page(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany", address="Yakovleva 5",
                    homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
                    email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))

    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany", address="Yakovleva 5",
                    homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
                    email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))

    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


'''1- Склеиваем при помощи перевода строки, 2 - Отфильтровываем пустые строки, 3 - Удаляет все лишние символы,
4 - Отфильтровываются все пусты (None), 5 - Исходный список из 4 элементов'''
def merge_phones_like_on_home_page(contact):
    return "\n".join(  #
        filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


''' Отсекаем лишние знаки (скобки, -, пробел и т.д.), "+" не отчищаем потому что он виден на главной странице
    1 параметр = что заменять, 2 = на что заменять (на пустую строчку ""), 3 = где заменять'''
def clear(s):
    return re.sub("[() -]", "", s)



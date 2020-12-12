from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import re
from random import randrange

def test_contact_check_main_page_and_edit_page_by_index(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_new_contact(
            Contact(firstname="Gleb", middlename="Alex", lastname="Kazarkin", nickname="gkazarkin", title="AccTitle",
                    company="TestCompany", address="Yakovleva 5",
                    homephone="515232", mobilephone="89539235812", workphone="367412", fax="89539234611",
                    email="gkazarkin@test.ru", email2="gkazarkin@test.com", homepage="gkazarkin.com", bday="11", bmonth="April", byear="1987", aday="11",
                    amonth="April", ayear="1987", address2="Yakovleva 5", secondaryphone="515232", notes="Test Note"))
    old_contacts = app.contact.get_contact_list()
    '''Генерируем случайный индекс от 0 до количества контактов'''
    index = randrange(len(old_contacts))

    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


'''1- Склеиваем при помощи перевода строки, 2- Отфильтровываем пустые строки, 3- Удаляет все лишние символы,
4- Отфильтровываются все пусты (None), 5- Исходный список из 4 элементов'''
def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


'''Отсекаем лишние знаки (скобки, -, пробел и т.д.), "+" не очищаем потому что он виден на главной странице
1 параметр = что заменять, 2 = на что заменять (на пустую строчку ""), 3 = где заменять'''
def clear(s):
    return re.sub("[() -]", "", s)

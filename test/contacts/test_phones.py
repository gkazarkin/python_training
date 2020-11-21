from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import re

# def test_old_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
#     assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
#     assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
#     assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def merge_phones_like_on_home_page(contact):
    return "\n".join(  # Склеиваем при помощи перевода строки
        filter(lambda x: x != "",  # Отфильтровываем пустые строки
                            map(lambda x: clear(x),  # Удаляет все лишние символы
                                filter(lambda x: x is not None,  # Отфильтровываются все пусты (None)
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))  # Исходный список из 4 элементов

def clear(s):
    # Отсекаем лишние знаки (скобки, -, пробел и т.д.), "+" не отчищаем потому что он виден на главной странице
    # 1 параметр = что заменять, 2 = на что заменять (на пустую строчку ""), 3 = где заменять
    return re.sub("[() -]", "", s)



# from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


""" Сколько контактов входит в группу"""
try:
    l = db.get_contacts_in_group(Group(id="330"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

""" Сколько контактов не входит в группу"""
try:
    l = db.get_contacts_not_in_group(Group(id="330"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
"""Группы"""
# try:
#     l = db.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass
#     # db.destroy()

"""Контакты"""
# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()

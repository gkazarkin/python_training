# from fixture.db import DbFixture
from fixture.orm import ORMFixture

# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

"""Контакты"""
try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    # db.destroy()

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

from model.contactsredata import ContactsRedata
import pytest
from fixture.contact import ContactHelper

def test_modify_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(ContactsRedata(title="ContactTitle"))
    app.session.log_out()

def test_modify_home_number(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(ContactsRedata(home="415212"))
    app.session.log_out()

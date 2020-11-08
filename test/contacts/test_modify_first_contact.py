from model.contactsredata import ContactsRedata
import pytest
from fixture.contact import ContactHelper

def test_modify_title(app):
    app.contact.modify_first_contact(ContactsRedata(title="ContactTitle"))

def test_modify_home_number(app):
    app.contact.modify_first_contact(ContactsRedata(home="415212"))

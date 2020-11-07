import pytest

def test_add_acc(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_first_contact()
    app.session.log_out()

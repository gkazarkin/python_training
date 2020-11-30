from model.contact import Contact
import pytest
from fixture.contact_methods import ContactHelper
import random
import string

def random_string(maxlen):
    """Генерируем символы"""
    gen_string = string.ascii_letters

    """Выбирает символы и склеивает этот список без пробелов через join в строку"""
    return "".join([random.choice(gen_string) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    gen_digits = str(string.digits)
    return "".join([random.choice(gen_digits) for i in range(random.randrange(maxlen))])

# def random_symbols(prefix, maxlen):
def random_symbols(maxlen):
    gen_symbols = string.ascii_letters + str(string.digits)
    # return prefix + "".join([random.choice(gen_symbols) for i in range(random.randrange(maxlen))])
    return "".join([random.choice(gen_symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    gen_email = string.ascii_letters + str(string.digits)
    return ("".join([random.choice(gen_email) for i in range(random.randrange(maxlen))])) + "@" +\
           ("".join([random.choice(gen_email) for i in range(random.randrange(maxlen))])) + ".ru"


""" list comprehension, цикл 2 раза """
contact_testdata = [
        Contact(firstname=random_string(10), middlename=random_string(10), lastname=random_string(10),
                nickname=random_symbols(10), title=random_symbols(10), company=random_symbols(10),
                address=random_symbols(10), homephone=random_digits(6), mobilephone=random_digits(11),
                workphone=random_digits(6), fax=random_digits(6), email=random_email(7),  email2=random_email(7),  email3=random_email(7),
                homepage=random_email(8), bday="11", bmonth="April", byear="1987", aday="11", amonth="April", ayear="1987",
                address2=random_symbols(10), secondaryphone=random_digits(11), notes=random_symbols(10))
        for name in range(2)
    ]

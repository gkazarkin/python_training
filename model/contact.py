from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, title=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address2=None, secondaryphone=None, notes=None,
                 all_emails_from_home_page=None, all_phones_from_home_page=None, id=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.title = title
        self.address = address

        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax

        self.email = email
        self.email2 = email2
        self.email3 = email3

        self.homepage = homepage
        self.bday = bday
        self.byear = byear
        self.bmonth = bmonth
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear

        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    """Представление объекта в консоли"""
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    """Логическое сравнение, вместо сравнения объектов в памяти"""
    def __eq__(self, other):
        """2 контакта равны, если совпадают имена"""
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            """максимальное число, которое может использоваться в индексах списков"""
            return maxsize

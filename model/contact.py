from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, title=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None, homepage=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address2=None, secondaryphone=None, notes=None,
                 all_phones_from_home_page=None, id=None):

        # self.firstname = firstname
        # self.lastname = lastname
        # self.homephone = homephone
        # self.mobilephone = mobilephone
        # self.workphone = workphone
        # self.secondaryphone = secondaryphone
        # self.all_phones_from_home_page = all_phones_from_home_page
        # self.id = id

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
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):  # Представление объекта в консоли
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):  # Логическое сравнение, вместо сравнения объектов в памяти
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname  # 2 контакта равны, если совпадают имена

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize  # максимальное число, которое может использоваться в индексах списков

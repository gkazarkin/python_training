import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        """Autocommit=True сбрасывает кеш"""
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                """Присвоится значени сразу в 4 переменные, каждой из них будет присвоен соответствующий элемент картежа"""
                (id, name, header, footer) = row
                """Помещает данные в список"""
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            """Остальные параметры добавить позже
            Отсекаем удалённые группы (у них deprecated=дата_удаления"""
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, "
                           "fax, email, email2, email3, homepage, address2, phone2, notes from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                """Присвоится значени сразу в все переменные, каждой из них будет присвоен соответствующий элемент картежа"""
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2,
                 email3, homepage, address2, phone2, notes) = row
                """Помещает данные в список"""
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                    company=company, title=title, address=address, homephone=home, mobilephone=mobile,
                                    workphone=work, fax=fax, email=email, email2=email2, email3=email3, homepage=homepage,
                                    address2=address2, secondaryphone=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()



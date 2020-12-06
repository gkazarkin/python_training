from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    """Описываем объектами структуру базы данных групп"""
    class ORMGroup(db.Entity):
        """Название таблицы и нужных столбцов"""
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        """Название таблицы и нужных столбцов"""
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    """conv=decoders разрешает pymysql конвертировать даты, а не ponyorm"""
    def __init__(self, host, name, user, password):
        """Привязка к базе данных в конструкторе"""
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        """Сопоставление свойств описанных классов с таблицей и её полями"""
        self.db.generate_mapping()
        sql_debug(True)

    """Преобразовываем из объекта типа ORMGroup в Group"""
    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        """list преобразовывает в список"""
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        """list преобразовывает в список"""
        return list(map(convert, contacts))

    """Функция, которая получает списки объектов, не надо писать SQL запрос, он геннерируется автоматически,
    а выборка берётся как будто из list comprehension"""
    @db_session
    def get_group_list(self):
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))
        # with db_session:
        #     return list(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))


from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    """представление объекта в памяти"""
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    """логическое сравнение вместо сравнения объектов в памяти"""
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name  # 2 группы равны если совпадают имена

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            """максимальное число, которое может использоваться в индексах списков"""
            return maxsize





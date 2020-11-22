from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):  # представление объекта в памяти
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):  # логическое сравнение вместо сравнения объектов в памяти
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name  # 2 группы равны если совпадают имена

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize  # максимальное число, которое может использоваться в индексах списков





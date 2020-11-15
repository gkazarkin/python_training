from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):  # predstavlenie objecta v console
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):  # logi4eskoe sravnenie, vmesto sravnenie objectov v pamyati
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name  # 2 groups ravni esli sovpadaut imena i id (daje esli id=None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize  # maximalnoe 4islo, kotoroe mojet ispolzovatsya v indexah spiskov





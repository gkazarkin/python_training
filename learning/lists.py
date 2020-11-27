

""" Списки, для однородных данных"""
list1 = [11, 22, 33, 44]
print(list1[0])
list2 = ["Moscow", "Berlin", "London"]
print(list2[1])

"""Кортеж"""
tuple1 = ("Windows", "8.1")
print(tuple1[0])

"""Словарь"""
d = {"os": "Windows", "os_version": "8.1"}
print(d["os_version"])
"""Вложенный словарь"""
d = {'os': {'type': 'Windows', 'version': '8.1'}, "browser": {'type': 'firefox', 'version': '35.0.1'}}
print(d['os']['type'])

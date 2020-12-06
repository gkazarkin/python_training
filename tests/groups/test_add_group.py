# -*- coding: utf-8 -*-
import pytest
from model.group import Group

"""Взятие списка групп из базы данных"""
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)

    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    """Опциональный флаг проверки через UI
        Прописать запуск можно или в консоли или справа вверху Edit_Configuration - Additional arguments (Options) --check_ui"""
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


"""Сравнивает список групп в UI"""
# def test_add_group(app, json_groups):
#     old_groups = app.group.get_group_list()
#     app.group.create(json_groups)
#
#     """Выступает в роли хеширования количества групп"""
#     assert len(old_groups) + 1 == app.group.count_groups()
#     new_groups = app.group.get_group_list()
#
#     old_groups.append(json_groups)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





"""Название параметра указывает на источник данных"""
# def test_add_group(app, data_groups):
#     # group = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(data_groups)
#
#     assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
#     new_groups = app.group.get_group_list()
#
#     old_groups.append(data_groups)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""Параметризация из сгенерированных данных в groups"""
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])  # Передаёт параметры и какие именно
# def test_add_group(app, group):
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#
#     assert len(old_groups) + 1 == app.group.count_groups()  # Выступает в роли хеширования количества групп
#     new_groups = app.group.get_group_list()
#
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)






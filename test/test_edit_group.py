# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_db(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='for_delete'))
    group_edit = Group(name='+Edit_name', footer='Edit footer', header='Edit header')
    old_groups = sorted(db.get_group_list(), key=Group.id_or_max)
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id, group_edit)
    new_groups = sorted(db.get_group_list(), key=Group.id_or_max)
    # сравнение через сортировку по id
    for i in new_groups:
        if i.id == group.id:
            assert i.name == group_edit.name
            assert i.footer == group_edit.footer
            assert i.header == group_edit.header
            # сравнение через изменение old
            old_groups[new_groups.index(i)] = Group(name='+Edit_name', footer='Edit footer', header='Edit header', id=group.id)
        assert(i == old_groups[new_groups.index(i)])
    if check_ui:
        ui_list = sorted(app.group.get_group_list(), key=Group.id_or_max)
        for i in range(len(new_groups)):
            assert ui_list[i].name == new_groups[i].name
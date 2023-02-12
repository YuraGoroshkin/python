# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='for_delete'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="+Edit_name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert old_groups != new_groups
    old_groups[index] = group
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


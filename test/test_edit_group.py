# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='for_delete'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="+Edit_name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name='for_edit'))
#     app.group.edit_first_group(Group(header="Header_edit"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='for_delete'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        ui_list = sorted(app.group.get_group_list(), key=Group.id_or_max)
        for i in range(len(new_groups)):
            assert ui_list[i].name == new_groups[i].name

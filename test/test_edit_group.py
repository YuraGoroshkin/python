# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="+Edit_name"))
    app.session.logout()


def test_edit_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="Header_edit"))
    app.session.logout()

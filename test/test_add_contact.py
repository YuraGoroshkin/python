# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.open_add_new()
    app.contact.add(contact)
    app.select_home()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

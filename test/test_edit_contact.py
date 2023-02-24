# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_edit_contact_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(firstname='firstname_edit', lastname='lastname_edit'))
    contact_new_edit = Contact(firstname='firstname',
                               lastname='lastname',
                               address='address'
                               )
    old_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, contact_new_edit)
    new_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(old_contacts) == len(new_contacts)

    for ind, i in enumerate(new_contacts):
        if i.id == contact.id:
            assert (
                    i.firstname == contact_new_edit.firstname and
                    i.lastname == contact_new_edit.lastname and
                    i.address == contact_new_edit.address
            )
        if check_ui:
            for k in app.contact.get_contact_list():
                if k.id == i.id:
                    assert (k == i)

# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new()
    app.contact.add(contact)
    app.select_home()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

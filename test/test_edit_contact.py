# -*- coding: utf-8 -*-
from model.contact import Contact
import time

def test_edit_first_contact(app):
    app.select_home()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.open_add_new()
        app.contact.add(
            Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                    company="Company", address="Address", telephone_home="88005553225", telephone_mobile="88005553225",
                    telephone_work="88005553225",
                    telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                    homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2", notes="Notes"))
        app.open_home_page()
    app.contact.edit_first_contact(
        Contact(firstname="correct33334"))
    app.select_home()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_empty(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new()
    app.contact.add(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                telephone_home="",
                telephone_mobile="", telephone_work="", telephone_fax="", email="", email2="", email3="", homepage="",
                byear="", ayear="",
                address2="", phone2="", notes=""))
    app.select_home()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new()
    app.contact.open_add_new()
    app.contact.add(
        Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                company="Company", address="Address", telephone_home="88005553225", telephone_mobile="88005553225",
                telephone_work="88005553225",
                telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2", notes="Notes"))
    app.select_home()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

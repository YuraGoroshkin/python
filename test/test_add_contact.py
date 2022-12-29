# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.select_add_new()
    app.contact.add(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                telephone_home="",
                telephone_mobile="", telephone_work="", telephone_fax="", email="", email2="", email3="", homepage="",
                byear="", ayear="",
                address2="", phone2="", notes=""))
    app.select_home()
    app.session.logout()


def test_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.select_add_new()
    app.contact.add(
        Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                company="Company", address="Address", telephone_home="88005553225", telephone_mobile="88005553225",
                telephone_work="88005553225",
                telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2", notes="Notes"))
    app.select_home()
    app.session.logout()

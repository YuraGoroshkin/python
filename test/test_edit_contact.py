# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="correct", middlename="correct", lastname="correct", nickname="correct", title="correct",
                company="correct", address="correct",
                TelephoneHome="correct",
                TelephoneMobile="correct", TelephoneWork="", TelephoneFax="correct", email="correct", email2="correct",
                email3="correct", homepage="correct",
                byear="correct", ayear="correct",
                address2="correct", phone2="correct", notes="correct"))
    app.select_home()
    app.session.logout()
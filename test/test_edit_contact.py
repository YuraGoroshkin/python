# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.select_home()
    if app.contact.count() == 0:
        app.contact.select_add_new()
        app.contact.add(
            Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                    company="Company", address="Address", telephone_home="88005553225", telephone_mobile="88005553225",
                    telephone_work="88005553225",
                    telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                    homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2", notes="Notes"))
        app.open_home_page()
    app.contact.edit_first_contact(
        Contact(firstname="correct", middlename="correct", lastname="correct", nickname="correct", title="correct",
                company="correct", address="correct",
                telephone_home="correct",
                telephone_mobile="correct", telephone_work="", telephone_fax="correct", email="correct",
                email2="correct",
                email3="correct", homepage="correct",
                byear="correct", ayear="correct",
                address2="correct", phone2="correct", notes="correct"))

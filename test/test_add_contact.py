# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_empty(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.select_add_new()
    app.contact.add(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", TelephoneHome="",
                TelephoneMobile="", TelephoneWork="", TelephoneFax="", email="", email2="", email3="", homepage="", byear="", ayear="",
                address2="", phone2="", notes=""))
    app.select_home()
    app.session.logout()


def test_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.select_add_new()
    app.contact.add(
        Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                company="Company", address="Address", TelephoneHome="88005553225", TelephoneMobile="88005553225", TelephoneWork="88005553225",
                TelephoneFax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2", notes="Notes"))
    app.select_home()
    app.session.logout()

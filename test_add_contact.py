# -*- coding: utf-8 -*-
from contact import Contact
from application2 import Application2
import pytest
@pytest.fixture
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy2)
    return fixture
def test_contact_empty(app2):
    app2.open_home_page()
    app2.login(username="admin", password="secret")
    app2.select_add_new()
    app2.add_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear="", address2="", phone2="", notes=""))
    app2.select_home()
    app2.logout()
def test_contact(app2):
    app2.open_home_page()
    app2.login(username="admin", password="secret")
    app2.select_add_new()
    app2.add_new_contact(Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title", company="Company", address="Address", home="88005553225", mobile="88005553225", work="88005553225", fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com", homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2", notes="Notes"))
    app2.select_home()
    app2.logout()

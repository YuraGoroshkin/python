# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
from model.group import Group


def test_add_contact_to_some_group(app, db, check_ui):
    # перешли на нужную страницу
    app.select_home()
    # проверил контакт и группу ,если нет  то создал
    if len(db.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.add(
            Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                    company="Company", address="Address", telephone_home="88005553225", telephone_mobile="88005553225",
                    telephone_work="88005553225",
                    telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                    homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2",
                    notes="Notes"))
        app.open_home_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='the_only'))
        app.open_home_page()
    old_contacts = db.get_contact_list()
    # обозначил какой контакт будет выбран для теста
    index = randrange(len(old_contacts))
    # выбрать группу
    #
    app.contact.put_contact_by_index_to_group(index)
    app.select_home()
    # assert len(old_contacts) == len(new_contacts)
    # if check_ui:
    #     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

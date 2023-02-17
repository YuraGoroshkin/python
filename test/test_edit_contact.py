# -*- coding: utf-8 -*-
from model.contact import Contact
import random



    index = randrange(len(old_contacts))
    contact = Contact(firstname="correct33334", lastname="Test")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    app.select_home()
    new_contacts = db.get_contact_list()
    assert old_contacts != new_contacts
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    def test_edit_some_contact(app, db, check_ui):
        app.select_home()
        if len(db.get_contact_list()) == 0:
            app.contact.open_add_new()
            app.contact.add(
                Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname",
                        title="Title",
                        company="Company", address="Address", telephone_home="88005553225",
                        telephone_mobile="88005553225",
                        telephone_work="88005553225",
                        telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                        homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2",
                        notes="Notes"))
            app.open_home_page()
        contact_edit = Contact(firstname="correct33334", lastname="Test")
        old_contacts =  sorted(db.get_contact_list(), key=Contact.id_or_max)
        contact = random.choice(old_contacts)
        app.contact.edit_contact_by_id
        app.group.edit_group_by_id(group.id, group_edit)
        new_groups = sorted(db.get_group_list(), key=Group.id_or_max)
        # сравнение каждой группы, через id, а затем по атрибутно
        for i in new_groups:
            if i.id == group.id:
                assert i.name == group_edit.name
                assert i.footer == group_edit.footer
                assert i.header == group_edit.header
            assert (i == old_groups[new_groups.index(i)])
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# -*- coding: utf-8 -*-
from model.contact import Contact


# def test_contact_empty(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.open_add_new()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
#                       telephone_home="",
#                       telephone_mobile="", telephone_work="", telephone_fax="", email="", email2="", email3="",
#                       homepage="",
#                       byear="", ayear="",
#                       address2="", phone2="", notes="")
#     app.contact.add(contact)
#     app.select_home()
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact(app):
    old_contacts_size = app.contact.get_contact_list()[1]
    old_contacts = app.contact.get_contact_list()[0]
    print('\n')
    print(old_contacts)
    app.contact.open_add_new()
    contact = Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname",
                      title="Title",
                      company="Company", address="Address", telephone_home="88005553225",
                      telephone_mobile="88005553225",
                      telephone_work="88005553225",
                      telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                      homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2",
                      notes="Notes")
    app.contact.add(contact)
    app.select_home()
    new_contacts_size = app.contact.get_contact_list()[1]
    assert old_contacts_size + 1 == new_contacts_size
    # new_contacts = app.contact.get_contact_list()[0]
    # old_contacts.append(contact)
    print('\n')
    print(contact)
    # old_contacts.append(contact)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

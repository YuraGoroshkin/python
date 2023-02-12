import re
from random import randrange
from model.contact import Contact


# def test_phones_on_home_page(app):
#     all_contacts = app.contact.get_contact_list()
#     index = randrange(len(all_contacts))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert clear_email(contact_from_home_page.email) == clear_email(merge_email_like_on_home_page(contact_from_edit_page))
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_phones_on_home_page_with_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    number_iteration = len(contact_from_home_page)
    i = 0
    while i < number_iteration:
        from_home_page = contact_from_home_page[i]
        from_database = contact_from_bd[i]
        i = i + 1
        assert from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(from_database)
        assert clear_email(from_home_page.email) == clear_email(merge_email_like_on_home_page(from_database))
        assert from_home_page.address == from_database.address
        assert from_home_page.firstname == from_database.firstname
        assert from_home_page.lastname == from_database.lastname



# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[()  -]", "", s)


def clear_email(s):
    return " ".join(s.split())


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))

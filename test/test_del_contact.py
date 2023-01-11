from model.contact import Contact
import time


def test_delete_first_contact(app):
    app.select_home()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.open_add_new()
        app.contact.add(
            Contact(firstname="correct", middlename="correct", lastname="correct", nickname="correct", title="correct",
                    company="correct", address="correct",
                    telephone_home="correct",
                    telephone_mobile="correct", telephone_work="", telephone_fax="correct", email="correct",
                    email2="correct",
                    email3="correct", homepage="correct",
                    byear="correct", ayear="correct",
                    address2="correct", phone2="correct", notes="correct"))
        app.open_home_page()
    app.contact.delete_first_contact()
    time.sleep(3)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)

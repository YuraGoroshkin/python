import random
from model.contact import Contact
import time
from random import randrange


def test_delete_some_contact(app, db):
    app.select_home()
    if len(db.get_contact_list()) == 0:
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
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(3)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

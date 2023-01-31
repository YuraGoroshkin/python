import random
import string
from model.contact import Contact

constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1",
            nickname="nickname1", title="title1", company="company1", address="address1",
            telephone_home="telephone_home1",
            telephone_mobile="telephone_mobile1", telephone_work="telephone_work1", telephone_fax="telephone_fax1",
            email="", email2="", email3="",
            homepage="homepage1",
            byear="byear1", ayear="ayear1",
            address2="address2", phone2="phone2", notes="notes")
]


def random_phone_number():
    number = str(random.randrange(9000000000, 9999999999))
    return '8' + number


def random_year():
    number = str(random.randrange(1000, 3000))
    return number


def random_email():
    email = ''
    for i in range(10):
        email += chr(random.randint(97, 122))

    return email + '@example.com'


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    telephone_home="",
                    telephone_mobile="", telephone_work="", telephone_fax="", email="", email2="", email3="",
                    homepage="",
                    byear="", ayear="",
                    address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 10), company=random_string("company", 10),
                       address=random_string("address", 10), telephone_home=random_phone_number(),
                       telephone_mobile=random_phone_number(),
                       telephone_work=random_phone_number(),
                       telephone_fax=random_phone_number(), email=random_email(),
                       email2=random_email(), email3=random_email(),
                       homepage=random_string("homepage", 10), byear=random_year(),
                       ayear=random_year(), address2=random_string("address2", 10),
                       phone2=random_phone_number(), notes=random_string("notes", 10))
               for i in range(10)]

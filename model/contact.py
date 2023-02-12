from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, telephone_home=None, telephone_mobile=None, telephone_work=None, telephone_fax=None,
                 email=None, email2=None, email3=None, homepage=None, byear=None, ayear=None, address2=None,
                 phone2=None, notes=None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = telephone_home
        self.mobile = telephone_mobile
        self.work = telephone_work
        self.fax = telephone_fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
            (self.id, self.firstname, self.lastname, self.middlename, self.nickname, self.title, self.company,
             self.address, self.home, self.mobile, self.work, self.fax, self.email, self.email2,
             self.email3, self.homepage, self.byear, self.ayear,
             self.address2,
             self.phone2, self.notes)

    # def __eq__(self, other):
    #     return (
    #                 self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

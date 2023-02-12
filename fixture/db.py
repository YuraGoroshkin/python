import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename, nickname, title, company, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, phone2, notes from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, title, company,
                 address, home, mobile, work, fax, email, email2,
                 email3, homepage, byear, ayear,
                 address2,
                 phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, title=title,
                                    company=company, address=address,
                                    telephone_home=home,
                                    telephone_mobile=mobile, telephone_work=work, telephone_fax=fax,
                                    email=email,
                                    email2=email2,
                                    email3=email3, homepage=homepage,
                                    byear=byear, ayear=ayear,
                                    address2=address2, phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def address_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                list.append(row)
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

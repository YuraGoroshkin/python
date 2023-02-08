from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.contact_form(contact)
        self.select_content()
        wd.find_element_by_id("container").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit delete via xpath
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        # window selection accept
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit delete via xpath
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        # window selection accept
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # select first contact
        self.select_contact_by_index(index)
        # +2 потому-что первый элемент на редактирование = 2 в блоке tr
        index_pencil = str(index + 2)
        # submit edit via xpath
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[' + index_pencil + ']/td[8]/a/img').click()
        self.contact_form(contact)
        self.select_content()
        # select update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            # open groups page
            wd.find_element_by_link_text("add new").click()

    def select_content(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_contact_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            # fill group form
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def contact_form(self, contact):
        wd = self.app.wd
        # form edit
        self.change_contact_form_value("firstname", contact.firstname)
        self.change_contact_form_value("middlename", contact.middlename)
        self.change_contact_form_value("lastname", contact.lastname)
        self.change_contact_form_value("nickname", contact.nickname)
        self.change_contact_form_value("title", contact.title)
        self.change_contact_form_value("company", contact.company)
        self.change_contact_form_value("address", contact.address)
        self.change_contact_form_value("home", contact.home)
        self.change_contact_form_value("mobile", contact.mobile)
        self.change_contact_form_value("work", contact.work)
        self.change_contact_form_value("fax", contact.fax)
        self.change_contact_form_value("email", contact.email)
        self.change_contact_form_value("email2", contact.email2)
        self.change_contact_form_value("email3", contact.email3)
        self.change_contact_form_value("homepage", contact.homepage)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='10']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='March']").click()
        self.change_contact_form_value("byear", contact.byear)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[12]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[7]").click()
        self.change_contact_form_value("ayear", contact.ayear)
        self.change_contact_form_value("address2", contact.address2)
        self.change_contact_form_value("phone2", contact.phone2)
        self.change_contact_form_value("notes", contact.notes)
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id,
                            all_phones_from_home_page=all_phones, address=all_address, email=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.select_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.select_home()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       telephone_home=homephone, telephone_work=workphone, telephone_mobile=mobilephone,
                       phone2=secondaryphone, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(telephone_home=homephone, telephone_work=workphone, telephone_mobile=mobilephone,
                       phone2=secondaryphone)

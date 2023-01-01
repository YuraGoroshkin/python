from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.contact_form(contact)
        self.select_content()
        wd.find_element_by_id("container").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit delete via xpath
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        # window selection accept
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit edit via xpath
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img').click()
        self.contact_form(contact)
        self.select_content()
        # select update
        wd.find_element_by_name("update").click()

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

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(0.1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    # Перейти на home page с другой страницы
    def select_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        # исключение при потери браузера
        try:
            self.wd.current_url
            return True
        except:
            print("ERROR_БРАУЗЕР:нет доступа")
            return False

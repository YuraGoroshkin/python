from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    # параметры запуска (браузер)
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(0.3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    # Перейти на home page с другой страницы
    def select_home(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("selected[]")) > 0):
            # open home
            wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        # параметры запуска (стенд)
        wd = self.wd
        # open home page
        wd.get(self.base_url)

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

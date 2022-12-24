from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import  GroupHalper
class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHalper(self)

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")
    def destroy(self):
        self.wd.quit()
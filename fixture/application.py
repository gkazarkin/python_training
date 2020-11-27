from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session_methods import SessionHelper
from fixture.group_methods import GroupHelper
from fixture.contact_methods import ContactHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome("C:\\chromedriver.exe")
        elif browser == "firefox":
            self.wd = webdriver.Firefox("C:\\geckodriver.exe")
        elif browser == "opera":
            self.wd = webdriver.Opera("C:\\operadriver.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie("C:\\IEDriverServer.exe")
        else:
            raise ValueError("Unrecognized browser %s" % browser)  # Исключение
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        get_main_page = wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    # def decorator_screenshot(func):
    #     def wrapper(*args, **kwargs):
    #         try:
    #            func(*args, **kwargs)
    #         except AssertionError:
    #             file_name = f'{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    #             driver.save_screenshot(file_name)
    #             raise
    #     return wrapper
    #
    # @decorator_screenshot
    # def test_something(self):
    #     Assert.fail("failed test")
    #
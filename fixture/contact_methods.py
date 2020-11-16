from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self, data):
        wd = self.app.wd
        self.click_add_new_contact()
        self.fill_contact_form(data)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contacts_page()

    def check_added_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("next birthdays").click()
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def modify_first_contact(self, data):
        wd = self.app.wd
        wd.find_element_by_css_selector("#maintable > tbody > tr:nth-child(2) > td:nth-child(7) > a").click()
        wd.find_element_by_name("modifiy").click()

        self.fill_contact_form(data)

        wd.find_element_by_name("update").click()

        wd.find_element_by_link_text("home page").click()

    def fill_contact_form(self, data):
        wd = self.app.wd
        self.change_field_value("firstname", data.firstname)
        self.change_field_value("middlename", data.middlename)
        self.change_field_value("lastname", data.lastname)
        self.change_field_value("nickname", data.nickname)
        self.change_field_value("title", data.title)
        self.change_field_value("company", data.company)
        self.change_field_value("address", data.address)
        self.change_field_value("home", data.home)
        self.change_field_value("mobile", data.mobile)
        self.change_field_value("work", data.work)
        self.change_field_value("fax", data.fax)
        self.change_field_value("email", data.email)
        self.change_field_value("email2", data.email2)
        self.change_field_value("homepage", data.homepage)

        self.select_date("bday", data.bday)
        self.select_date("bmonth", data.bmonth)
        self.change_field_value("byear", data.byear)

        self.select_date("aday", data.aday)
        self.select_date("amonth", data.amonth)
        self.change_field_value("ayear", data.ayear)

        self.change_field_value("address2", data.address2)
        self.change_field_value("phone2", data.phone2)
        self.change_field_value("notes", data.notes)

    def click_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_date(self, field_name, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(date)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("#content > form:nth-child(10) > div:nth-child(8) > input[type=button]").click()
        # wd.switch_to_alert().accept()
        wd.switch_to.alert.accept()
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        # Проверяем находимся ли мы уже на странице контактов и если нет, то переходим
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()


    def count_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("entry")
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            firstname = wd.find_element_by_css_selector("#maintable > tbody > tr:last-child > td:nth-child(3)").text
            lastname = wd.find_element_by_css_selector("#maintable > tbody > tr:last-child > td:nth-child(2)").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts




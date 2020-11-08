from selenium.webdriver.support.ui import Select
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self, acc):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(acc.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(acc.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(acc.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(acc.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(acc.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(acc.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(acc.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(acc.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(acc.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(acc.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(acc.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(acc.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(acc.email2)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(acc.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(acc.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(acc.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(acc.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(acc.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(acc.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(acc.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(acc.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(acc.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(acc.notes)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contacts_page()

    def check_added_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("next birthdays").click()
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def modify_first_contact(self, contactsredata):
        wd = self.app.wd
        wd.find_element_by_css_selector("#maintable > tbody > tr:nth-child(2) > td:nth-child(7) > a").click()
        wd.find_element_by_name("modifiy").click()

        self.fill_contact_form(contactsredata)

        wd.find_element_by_name("update").click()

        wd.find_element_by_link_text("home page").click()

    def fill_contact_form(self, contactsredata):
        wd = self.app.wd
        self.change_field_value("firstname", contactsredata.home)
        self.change_field_value("middlename", contactsredata.middlename)
        self.change_field_value("lastname", contactsredata.lastname)
        self.change_field_value("nickname", contactsredata.nickname)
        self.change_field_value("title", contactsredata.title)
        self.change_field_value("company", contactsredata.company)
        self.change_field_value("address", contactsredata.address)
        self.change_field_value("home", contactsredata.home)
        self.change_field_value("mobile", contactsredata.mobile)
        self.change_field_value("work", contactsredata.work)
        self.change_field_value("fax", contactsredata.fax)
        self.change_field_value("email", contactsredata.email)
        self.change_field_value("email2", contactsredata.email2)
        self.change_field_value("homepage", contactsredata.homepage)
        # deleted birthday, anniversary
        self.change_field_value("ayear", contactsredata.ayear)
        self.change_field_value("address2", contactsredata.address2)
        self.change_field_value("phone2", contactsredata.phone2)
        self.change_field_value("notes", contactsredata.notes)

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
        wd.switch_to_alert().accept()
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))




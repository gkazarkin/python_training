from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None  # Кеширование списка контактов, сбрасывается после добавления\удаления\модификации

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            find_contacts = wd.find_elements_by_name("entry")
            for row in find_contacts:
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                # id = row.find_element_by_name("selected[]").get_attribute("value")  # У чекбоксов находим value
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)

    def add_new_contact(self, data):
        wd = self.app.wd
        self.click_add_new_contact()
        self.fill_contact_form(data)
        click_enter = wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

        self.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index, data):
        wd = self.app.wd
        self.open_contact_page_and_click_edit_contact(index)

        self.fill_contact_form(data)
        click_update = wd.find_element_by_name("update").click()

        click_home = wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def open_contact_page_and_click_edit_contact(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell_to_edit = row.find_elements_by_tag_name("td")[7]
        click_edit = cell_to_edit.find_element_by_tag_name("a").click()

    # def open_contact_to_edit_by_index(self, index, data):
    #     wd = self.app.wd
    #     find_contacts = wd.find_elements_by_name("entry")
    #     # click_edit = find_contacts[index].find_element_by_xpath("./td[8]/a/img").click()
    #     cells = find_contacts[index].find_elements_by_tag_name("td")
    #     click_edit = cells[7].find_element_by_css_selector("a").click()
    #
    #     self.fill_contact_form(data)
    #     click_update = wd.find_element_by_name("update").click()
    #
    #     click_home = wd.find_element_by_link_text("home page").click()
    #     self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        click_view = cell.find_element_by_tag_name("a").click()




    def modify_first_contact(self, data):
        self.open_contact_to_edit_by_index(0, data)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        click_delete = wd.find_element_by_css_selector("#content > form:nth-child(10) > div:nth-child(8) > input[type=button]").click()
        # wd.switch_to_alert().accept()
        close_alert = wd.switch_to.alert.accept()

        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        checkbox = wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        checkbox = wd.find_element_by_name("selected[]").click()

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
        click_add_new = wd.find_element_by_link_text("add new").click()

    def select_date(self, field_name, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(date)

    def open_home_page(self):
        wd = self.app.wd
        # Проверяем находимся ли мы уже на странице контактов и если нет, то переходим
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            click_home = wd.find_element_by_link_text("home").click()

    def count_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))








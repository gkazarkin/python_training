from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    """Кеширование списка контактов, сбрасывается после добавления или удаления или модификации"""
    contact_cache = None

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
                address = cells[3].text
                all_emails = cells[4].text

                """У чекбоксов находим value"""
                # id = row.find_element_by_name("selected[]").get_attribute("value")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")

                """Делим все телефоны на строки в список"""
                # all_phones = cells[5].text.splitlines()
                # print("contact's phones from main page = " + str(all_phones))  # = ['515232', '89539235812', '367412', '515232']
                # self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, homephone=all_phones[0],
                #                                   mobilephone=all_phones[1], workphone=all_phones[2], secondaryphone=all_phones[3]))
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def add_new_contact(self, data):
        wd = self.app.wd
        self.click_add_new_contact()
        self.fill_contact_form(data)
        click_enter = wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

        self.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()

        # row = wd.find_elements_by_name("entry").find_element_by_css_selector("input[value='%s']" % id)
        row = wd.find_element_by_css_selector("input[value='%s']" % id)
        cell_to_edit = row.find_elements_by_tag_name("td")[7]
        click_edit = cell_to_edit.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell_to_edit = row.find_elements_by_tag_name("td")[7]
        click_edit = cell_to_edit.find_element_by_tag_name("a").click()

    def modify_contact_by_id(self, id, data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)

        self.fill_contact_form(data)
        click_update = wd.find_element_by_name("update").click()

        click_home = wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def modify_contact_by_index(self, index, data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)

        self.fill_contact_form(data)
        click_update = wd.find_element_by_name("update").click()

        click_home = wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        click_view = cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        """Строим объект, 1 = название параметра, 2 = название локальной переменной"""
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)

        """Тут телефоны не идут отдельно, а идут скопом со всеми данными контакта"""
        text = wd.find_element_by_id("content").text

        """Ищем строку, начинающуюся с H: и берём значение до переноса строки"""
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)

        """Строим объект, 1 = название параметра, 2 = название локальной переменной"""
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def modify_first_contact(self, data):
        self.modify_contact_by_index(0, data)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        click_delete = wd.find_element_by_css_selector("#content > form:nth-child(10) > div:nth-child(8) > input[type=button]").click()
        # wd.switch_to_alert().accept()
        close_alert = wd.switch_to.alert.accept()

        self.open_home_page()
        self.contact_cache = None

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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        checkbox = wd.find_element_by_css_selector("input[value='%s']" % id).click()

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

        self.change_field_value("home", data.homephone)
        self.change_field_value("mobile", data.mobilephone)
        self.change_field_value("work", data.workphone)
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
        self.change_field_value("phone2", data.secondaryphone)
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

        """Проверяем находимся ли мы уже на странице контактов и если нет, то переходим"""
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            click_home = wd.find_element_by_link_text("home").click()

    def count_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))








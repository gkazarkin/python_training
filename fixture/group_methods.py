from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # Проверяем находимся ли мы уже на странице групп и если нет, то переходим
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()

        # init groups page
        click_new = wd.find_element_by_name("new").click()

        self.fill_group_form(group)

        # submit group creation
        click_submit = wd.find_element_by_name("submit").click()

        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()

        self.select_group_by_index(index)

        # open modification form
        click_edit = wd.find_element_by_name("edit").click()

        # fill group form
        self.fill_group_form(group)

        # submit modification
        click_update = wd.find_element_by_name("update").click()

        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, group):
        self.modify_group_by_index(0, group)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()

        self.select_group_by_index(index)

        # submit deletion
        click_delete = wd.find_element_by_name("delete").click()

        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        checkbox = wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        checkbox = wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, data):
        self.change_field_value("group_name", data.name)
        self.change_field_value("group_header", data.header)
        self.change_field_value("group_footer", data.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_groups_page(self):
        wd = self.app.wd
        click_groups = wd.find_element_by_link_text("group page").click()

    group_cache = None  # Кеширование списка групп, сбрасывается после добавления\удаления\модификации

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            wd.find_elements_by_css_selector("span.group")  # В консоли $$('span.group') -> найти элементы
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")  # У чекбокса находим value
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)



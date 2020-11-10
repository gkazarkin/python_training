

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()

        # init groups page
        wd.find_element_by_name("new").click()

        self.fill_group_form(group)

        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()

        self.select_first_group()

        # open modification form
        wd.find_element_by_name("edit").click()

        # fill group form
        self.fill_group_form(group)

        # submit modification
        wd.find_element_by_name("update").click()

        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()

        self.select_first_group()

        # submit deletion
        wd.find_element_by_name("delete").click()

        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

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
        wd.find_element_by_link_text("group page").click()
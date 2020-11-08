

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

    # def edit_first_group(self):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #
    #     wd.find_element_by_name("selected[]").click()
    #     wd.find_element_by_name("edit").click()
    #
    #     wd.find_element_by_name("group_name").click()
    #     wd.find_element_by_name("group_name").clear()
    #     wd.find_element_by_name("group_name").send_keys("test_group_edited")
    #
    #     wd.find_element_by_name("group_header").click()
    #     wd.find_element_by_name("group_header").clear()
    #     wd.find_element_by_name("group_header").send_keys("footer_edited")
    #
    #     wd.find_element_by_name("group_footer").click()
    #     wd.find_element_by_name("group_footer").clear()
    #     wd.find_element_by_name("group_footer").send_keys("footer_edited")
    #
    #     wd.find_element_by_name("update").click()
    #     self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()

        self.select_first_group()

        # submit deletion
        wd.find_element_by_name("delete").click()

        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()

        self.select_first_group()

        # open modification form
        wd.find_element_by_name("edit").click()

        # fill group form
        self.fill_group_form(new_group_data)

        # submit modification
        wd.find_element_by_name("update").click()

        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, groupredata):
        wd = self.app.wd
        self.change_field_value("group_name", groupredata.name)
        self.change_field_value("group_header", groupredata.header)
        self.change_field_value("group_footer", groupredata.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
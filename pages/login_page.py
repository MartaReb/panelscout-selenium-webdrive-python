from pages.base_page import BasePage


class LoginPage(BasePage):
    header_login_form_xpath = "//*[text()='Scouts Panel']"
    expected_header = "Scouts Panel"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    dropdown_language_list_xpath = "//*[contains(@class, 'MuiSelect-root')]"
    login_url = "https://scouts-test.futbolkolektyw.pl/login"
    expected_title = "Scouts panel - sign in"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def header_of_login_form(self):
        self.assert_element_text(self.driver, self.header_login_form_xpath, self.expected_header)





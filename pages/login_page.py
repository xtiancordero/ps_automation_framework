from pages.page_actions import PageActions
from locators.locators import LoginLocators

class LoginPage(PageActions):
   
    def login(self, username, password):
        self.input_text_to_field(LoginLocators.username, username)
        self.input_text_to_field(LoginLocators.password, password)
        self.click_button(LoginLocators.login_button)
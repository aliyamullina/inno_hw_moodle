import logging
from selenium.webdriver.remote.webelement import WebElement
from locators.auth_locators import LoginPageLocators
from locators.base_locators import BasePageLocators
from locators.personaldata_locators import PersonalDataPageLocators
from models.auth_model import AuthData
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def __init__(self, app):
        self.app = app

    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.confirm_exit_window():
            self.click_element(self.confirm_exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def confirm_exit(self):
        return self.find_element(BasePageLocators.CONFIRM_EXIT_BUTTON)

    def confirm_exit_window(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(BasePageLocators.CONFIRM_EXIT_BUTTON)
        if len(element) > 0:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN_INPUT)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD_INPUT)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.AUTH_BUTTON_SUBMIT)

    def auth_login_error(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    def go_to_editing_personal_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(PersonalDataPageLocators.EDIT_INFO))

    def user_menu_settings(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU_SETTINGS)

    def sign_out(self):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.confirm_exit_window():
            self.click_element(self.confirm_exit())

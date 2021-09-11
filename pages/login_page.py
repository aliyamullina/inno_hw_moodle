from locators.auth import LoginPageLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def auth(self, login: str, password: str):
        sign_in = self.app.driver.find_element(*LoginPageLocators.SIGN_IN)
        sign_in_link = sign_in.find_element(*LoginPageLocators.SIGN_IN_LINK)
        sign_in_link.click()

        login_input = self.app.driver.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.send_keys(login)

        password_input = self.app.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        auth_button_submit = self.app.driver.find_element(*LoginPageLocators.AUTH_BUTTON_SUBMIT)
        auth_button_submit.click()

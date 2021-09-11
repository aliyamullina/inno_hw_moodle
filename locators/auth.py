from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGN_IN = (By.CLASS_NAME, 'usermenu')
    SIGN_IN_LINK = (By.TAG_NAME, 'a')

    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    AUTH_BUTTON_SUBMIT = (By.ID, 'loginbtn')

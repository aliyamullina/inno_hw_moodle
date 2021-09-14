from selenium.webdriver.common.by import By


class AuthPageLocators:
    SIGN_IN = (By.CLASS_NAME, "usermenu")
    SIGN_IN_LINK = (By.TAG_NAME, "a")

    LOGIN_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    AUTH_BUTTON_SUBMIT = (By.ID, "loginbtn")

    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")

    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")

    LOGIN_ERROR = (By.ID, "loginerrormessage")
    USER_MENU_SETTINGS = (By.ID, "actionmenuaction-5")

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def click_element(self, element):
        element.click()

    def fill_element(self, element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    def find_select_element(self, locator):
        select_element = Select(self.find_element(locator))
        return select_element

    def find_clickable_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            expected_conditions.element_to_be_clickable(locator),
            message=f"Element not clickable {locator}",
        )
        return element

    def select_value(self, select_element, value):
        select_element.select_by_value(value)

    def click_enter(self, element):
        element.send_keys(Keys.RETURN)

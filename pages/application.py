from pages.auth_page import AuthPage
from pages.newcourse_page import NewCoursePage
from pages.personaldata_page import (
    PersonalDataPage,
    PersonalDataPageMore,
    PersonalDataPageOptional,
    PersonalDataPageTag,
)


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = AuthPage(self)
        self.personal_data = PersonalDataPage(self)
        self.personal_data_more = PersonalDataPageMore(self)
        self.personal_data_optional = PersonalDataPageOptional(self)
        self.personal_data_tag = PersonalDataPageTag(self)
        self.new_course = NewCoursePage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def quit(self):
        self.driver.quit()

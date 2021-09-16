from selenium.webdriver.remote.webelement import WebElement
from locators.newcourse_locators import NewCourseManagementLocators, NewCourseCreateLocators
from models.newcourse_model import NewCourse
from pages.base_page import BasePage


class NewCoursePage(BasePage):
    # Management new course
    def go_to_adding_new_course(self) -> None:
        self.click_element(self.admin_button())
        self.click_element(self.courses_button())
        self.click_element(self.add_new_course_button())

    def admin_button(self) -> WebElement:
        return self.get_clickable_element(NewCourseManagementLocators.ADMIN_BUTTON)

    def courses_button(self) -> WebElement:
        return self.find_element(NewCourseManagementLocators.COURSES_HEADER)

    def add_new_course_button(self) -> WebElement:
        return self.find_element(NewCourseManagementLocators.ADD_NEW_COURSE_BUTTON)

    # Create new course
    def create_new_course(self, new_course_data: NewCourse) -> None:
        self.fill_element(self.full_name_input(), new_course_data.full_name)
        self.fill_element(self.short_name_input(), new_course_data.short_name)
        self.fill_element(self.description_input(), new_course_data.description)
        self.click_element(self.save_and_display_button())

    def full_name_input(self) -> WebElement:
        return self.find_element(NewCourseCreateLocators.FULL_NAME)

    def short_name_input(self) -> WebElement:
        return self.find_element(NewCourseCreateLocators.SHORT_NAME)

    def description_input(self) -> WebElement:
        return self.find_element(NewCourseCreateLocators.DESCRIPTION)

    def save_and_display_button(self) -> WebElement:
        return self.find_element(NewCourseCreateLocators.SAVE_AND_DISPLAY_BUTTON)

    # Check create new course
    def is_course_exist(self, new_course_data: NewCourse) -> bool:
        elements = self.find_elements(NewCourseCreateLocators.CREATED_COURSE_NAME)
        new_course_list = [c.text for c in elements]
        if new_course_data.full_name in new_course_list:
            return True
        return False

    # Check empty fields
    def all_required_fields_filled(self) -> bool:
        if self.full_name_error_message() or self.short_name_error_message():
            return False
        return True

    def full_name_error_message(self) -> WebElement:
        return self.find_element(NewCourseCreateLocators.FULL_NAME_ERROR)

    def short_name_error_message(self) -> WebElement:
        return self.find_element(NewCourseCreateLocators.SHORT_NAME_ERROR)

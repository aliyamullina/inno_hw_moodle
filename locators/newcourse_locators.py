from selenium.webdriver.common.by import By


class NewCourseManagementLocators:
    ADMIN_BUTTON = (By.XPATH, "//span[text()='Администрирование']")
    COURSES_HEADER = (By.XPATH, "//a[@href='#linkcourses']")
    ADD_NEW_COURSE_BUTTON = (By.XPATH, "//a[text()='Добавить курс']")


class NewCourseCreateLocators:
    SIDEBAR_MENU = (By.ID, "nav-drawer")
    SIDEBAR_BUTTON = (By.CLASS_NAME, "btn")

    FULL_NAME = (By.ID, "id_fullname")
    SHORT_NAME = (By.ID, "id_shortname")
    DESCRIPTION = (By.ID, "id_summary_editoreditable")
    SAVE_AND_DISPLAY_BUTTON = (By.ID, "id_saveanddisplay")

    FULL_NAME_ERROR = (By.ID, "id_error_fullname")
    SHORT_NAME_ERROR = (By.ID, "id_error_shortname")

    CREATED_COURSE_NAME = (By.TAG_NAME, "h1")

    CREATE_COURSE_BUTTON = (By.XPATH, "//a[text()='Создать новый курс']")
    COURSE_DELETE_CONFIRMATION = (By.TAG_NAME, "h2")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")

    @staticmethod
    def get_course_locator(course_name):
        return By.XPATH, f"//a[text()='{course_name}']"

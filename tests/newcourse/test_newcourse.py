import pytest

from models.newcourse_model import NewCourse


class TestNewCourse:
    def test_create_new_course(self, app, auth):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Перейти на страницу создания курса.
        4. Создать курс с действительными данными.
        5. Убедиться, что курс успешно создан.
        6. Удалить курс.
        """
        app.new_course.go_to_adding_new_course()
        new_course_data = NewCourse.random()
        app.new_course.create_new_course(new_course_data)
        assert app.new_course.is_course_exist(
            new_course_data
        ), "No new course is created!"

    @pytest.mark.parametrize(
        "full_name, short_name",
        [
            ["Тестовое полное имя", ""],
            ["", "Тестовое короткое имя"],
        ],
    )
    def test_create_new_course_with_invalid_data(
        self, app, auth, full_name, short_name
    ):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Перейти на страницу создания курса.
        4. Создать курс с не действительными данными.
        5. Убедиться, что курс не создан.
        """
        app.new_course.go_to_adding_new_course()
        new_course_data = NewCourse.random()
        setattr(new_course_data, "full_name", full_name)
        setattr(new_course_data, "short_name", short_name)
        app.new_course.create_new_course(new_course_data)
        assert (
            not app.new_course.all_required_fields_filled()
        ), "Course is created with empty fields!"

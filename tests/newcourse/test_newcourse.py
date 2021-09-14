import pytest

from models.newcourse_model import NewCourse


@pytest.mark.new_course
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
        data = NewCourse.random()
        app.new_course.create_new_course(data)
        assert app.new_course.is_course_exist(data), "No new course is created!"

    @pytest.mark.parametrize(
        "full_name, short_name",
        [
            [NewCourse.random().short_name, ""],
            ["", NewCourse.random().full_name],
        ],
    )
    def test_create_new_course_with_empty_data(self, app, auth, full_name, short_name):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Перейти на страницу создания курса.
        4. Создать курс с пустыми данными.
        5. Убедиться, что курс не создан.
        """
        app.new_course.go_to_adding_new_course()
        data = NewCourse.random()
        setattr(data, "full_name", full_name)
        setattr(data, "short_name", short_name)
        app.new_course.create_new_course(data)
        assert (
            not app.new_course.all_required_fields_filled()
        ), "Course is created with empty fields!"

import pytest

from models.personaldata_model import PersonalData


@pytest.mark.personal_data
class TestPersonalData:
    def test_valid_edit_basic_personal_data(self, app, auth):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Отредактировать основные личные данные, указав действительные данные.
        6. Проверить успешное редактирование.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        app.personal_data.edit_personal_data(personal_data)
        assert app.personal_data.is_changed(), "Personal data not changed!"

    @pytest.mark.parametrize("field", ["name", "last_name", "email"])
    def test_edit_basic_personal_data_without_required_field(self, app, auth, field):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Редактировать основные личные данные с не действительными данными.
        6. Убедиться, что редактирование не прошло успешно.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        setattr(personal_data, field, "")
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize("email", ["mail", "@gmail.com", "0"])
    def test_edit_basic_personal_data_with_incorrect_email(self, app, auth, email):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Отредактировать основные личные данные с неверным email.
        6. Убедиться, что редактирование не прошло успешно.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        setattr(personal_data, "email", email)
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.parametrize(
        "name, last_name",
        [
            ["123", "123"],
            ["---", "---"],
            ["\xbdR6\x10\x7f", "\xbdR6\x10\x7f"],
            [PersonalData().random().url, PersonalData().random().url],
            [PersonalData().random().image_url, PersonalData().random().image_url],
        ],
    )
    def test_edit_incorrect_name_lastname(self, app, auth, name, last_name):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Изменить имя или (и) фамилию на цифры.
        6. Убедиться, что редактирование не прошло успешно.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        setattr(personal_data, "name", name)
        setattr(personal_data, "last_name", last_name)
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    def test_valid_edit_more_personal_data(self, app, auth):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Отредактировать дополнительные личные данные, указав действительные данные.
        6. Убедиться, что редактирование прошло успешно.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        app.personal_data_more.edit_personal_data_more(personal_data)
        assert app.personal_data_more.is_changed(), "Personal data not changed!"

    def test_valid_edit_optional_personal_data(self, app, auth):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Изменить необязательные личные данные, указав действительные данные.
        6. Убедиться, что редактирование прошло успешно.
        """
        app.open_main_page()
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        app.personal_data_optional.edit_personal_data_optional(personal_data)
        assert app.personal_data_optional.is_changed(), "Personal data not changed!"

    def test_valid_edit_tag_personal_data(self, app, auth):
        """
        Шаги.

        1. Открыть страницу авторизации.
        2. Авторизоваться с действительными данными.
        3. Проверить результат аутентификации.
        4. Перейти на страницу редактирования личных данных.
        5. Добавить тег с действительными данными.
        6. Убедиться, что редактирование прошло успешно.
        """
        app.open_main_page()
        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        app.personal_data_tag.edit_personal_data_tag(personal_data)
        assert app.personal_data_tag.is_changed(), "Personal data not changed!"

import pytest

from common.const import AuthConst
from models.auth import AuthData


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Шаги
        1. Открыть главную страницу
        2. Авторизоваться с действительными данными
        3. Проверить результат аутентификации
        """
        app.open_auth_page()
        data = AuthData(login='user_am@test.com', password='Psf2DrCMeG**')
        app.login.auth(data)
        assert app.login.is_auth(), 'We are not auth'

    def test_auth_invalid_data(self, app):
        """
        Шаги
         1. Открыть главную страницу
         2. Авторизоваться с не действительными данными
         3. Проверить результат аутентификации
        """
        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        assert AuthConst.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Шаги
         1. Открыть главную страницу
         2. Авторизоваться с пустыми данными
         3. Проверить результат аутентификации
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)
        app.login.auth(data)
        assert AuthConst.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from models.auth_model import AuthData
from pages.application import Application


@pytest.fixture(scope='session')
def app(request):
    base_url = request.config.getoption('--base-url')
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install()), base_url)
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--base-url',
        action='store',
        default='https://qacoursemoodle.innopolis.university/',
        help='enter base_url',
    ),
    parser.addoption(
        '--username',
        action='store',
        default='user_am@test.com',
        help='enter username',
    ),
    parser.addoption(
        '--password',
        default='Psf2DrCMeG**',
        help='enter password',
    ),


@pytest.fixture
def auth(app, request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    auth_data = AuthData(login=username, password=password)
    app.login.auth(auth_data)
    assert app.login.is_auth(), "You are not auth"
    yield
    app.login.sign_out()

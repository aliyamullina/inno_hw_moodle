import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth_model import AuthData
from pages.application import Application


@pytest.fixture(scope='session')
def app(request):
    base_url = request.config.getoption('--base-url')
    headless_mode = request.config.getoption("--headless").lower()

    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = True
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            base_url,
        )
    elif headless_mode == "false":
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()), base_url,
        )
    else:
        raise pytest.UsageError("--headless should be true or false")

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

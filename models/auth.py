from faker import Faker

fake = Faker("Ru-ru")


class AuthData:
    """
    Генерация пары логин и пароль с помощью faker
    """
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)

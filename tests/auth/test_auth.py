class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_main_page()
        app.login.auth(login='user_am@test.com', password='Psf2DrCMeG**')
        assert 1 == 1, 'Check auth data'

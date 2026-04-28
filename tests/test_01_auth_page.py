import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.auth_page import AuthPage
from pages.home_page import HomePage


@pytest.mark.parametrize('email, password', (('test@test.test', '123456789'), ('user@user.user', 'password')))
@pytest.mark.authorization
@pytest.mark.smoke
def test_user_can_authorize(
        fresh_browser: WebDriver,
        auth_page: AuthPage,
        home_page: HomePage,
        email: str,
        password: str
):
    home_page.visit('https://upstore24.ru/')

    home_page.click_auth_btn()

    auth_page.fill_the_inputs(email, password)
    try:
        auth_page.assert_main_word_and_result(auth_page.get_main_word(auth_page.main_word), 'История заказов')
        print('Вход в учетную запись!')
    except Exception:
        assert auth_page.check_error_msg() == 'Сочетание логина и пароля не подходит'


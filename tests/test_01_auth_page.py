from selenium.webdriver.chrome.webdriver import WebDriver
from pages.auth_page import AuthPage
from pages.home_page import HomePage


def test_user_can_authorize(browser: WebDriver, auth_page: AuthPage, home_page: HomePage):
    home_page.visit('https://upstore24.ru/')
    browser.maximize_window()

    home_page.select_open_window_close_btn()
    home_page.click_auth_btn()

    auth_page.fill_the_inputs(email='test@test.test', password='123456789')
    auth_page.assert_main_word_and_result(auth_page.get_main_word(auth_page.main_word), 'История заказов')
    print('Мы вошли в учетную запись!')


import allure
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.catalog_page import CatalogPage


@allure.description("Test guest can get in catalog page")
def test_guest_can_get_in_catalog_page(browser):
    """
    В данном тесте происходит нажатие на кнопку входа в учетную запись, заполняются поля с почтой и паролем на странице
    авторизации, нажимается 'Войти'. Проверка, удалось ли авторизоваться, через сравнение ap.main_word и словосочетания
    'История заказов' в методе assert_main_word_and_result. Возврат на главную страницу, нажатие на 'Каталог'
    и переход на страницу каталога.
    Если тест проходит assert-ы, то выводятся принты в консоль и сохраняются скриншот.
    """
    link = 'https://upstore24.ru/'
    browser.get(link)
    browser.maximize_window()

    hp = HomePage(browser)
    hp.select_open_window_close_btn()
    hp.click_auth_btn()

    ap = AuthPage(browser)
    ap.fill_the_inputs()
    ap.assert_main_word_and_result(ap.get_main_word(ap.main_word), 'История заказов')
    print('Мы вошли в учетную запись!')
    ap.get_screenshot()
    ap.click_logo_btn()

    hp.select_catalog_btn()

    cp = CatalogPage(browser)
    cp.assert_main_word_and_result(cp.get_main_word(cp.main_word), 'Каталог')
    print('Мы на странице каталога!')
    cp.get_screenshot()





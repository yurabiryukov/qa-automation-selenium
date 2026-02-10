import allure
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage


@allure.description("Test guest can get in catalog page")
def test_guest_can_get_in_catalog_page(browser):
    """
    В данном тесте мы находим вкладку 'Каталог' после того,
    как оказались на главной странице сайта https://upstore24.ru/, и нажимаем на нее,
    далее проверяем, произошел ли переход, через сравнение cp.main_word и слова 'Каталог'
    в методе assert_main_word_and_result.
    Если тест проходит assert, то выводится принт в консоль и сохраняется скриншот.
    """
    link = 'https://upstore24.ru/'
    browser.get(link)
    browser.maximize_window()

    hp = HomePage(browser)
    hp.select_open_window_close_btn()
    hp.select_catalog_btn()

    cp = CatalogPage(browser)
    cp.assert_main_word_and_result(cp.get_main_word(cp.main_word), 'Каталог')
    print('Мы на странице каталога!')
    cp.get_screenshot()





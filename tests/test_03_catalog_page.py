import allure, pytest, time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.catalog_page import CatalogPage
from pages.gadgets_page import GadgetsPage


@allure.description("Test guest can get in gadgets page")
def test_guest_can_get_in_gadgets_page(browser: WebDriver, catalog_page: CatalogPage, gadgets_page: GadgetsPage):

    catalog_page.visit('https://upstore24.ru/collection/all')

    catalog_page.select_gadgets_btn()

    gadgets_page.assert_main_word_and_result(gadgets_page.get_main_word(gadgets_page.main_word), 'Гаджеты')
    print('Мы на странице с гаджетами!')
    gadgets_page.get_screenshot()


@pytest.mark.parametrize('product_name', ('apple', 'фззду', '  xiaomi  ', '////'))
@allure.description("Test user can use search")
def test_user_can_use_search(browser: WebDriver, catalog_page: CatalogPage, product_name: str):

    catalog_page.visit('https://upstore24.ru/collection/all')

    catalog_page.fill_search_field(product_name)
    time.sleep(2)
    catalog_page.check_search_works_as_expected(product_name)

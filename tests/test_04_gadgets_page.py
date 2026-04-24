import allure, time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.gadgets_page import GadgetsPage
from pages.carts_page import CartsPage


@allure.description("Test user can add gadget to cart")
def test_user_can_add_gadget_to_cart(
        browser: WebDriver,
        gadgets_page: GadgetsPage,
        carts_page: CartsPage
):

    gadgets_page.visit('https://upstore24.ru/collection/gadgets')

    gadgets_page.select_open_window_close_btn()
    # Сохраняем наименование и стоимость товара со страницы с гаджетами для сравнения с корзиной
    name_on_gadget_page = gadgets_page.get_item_name()
    price_on_gadget_page = gadgets_page.get_item_price()
    gadgets_page.select_item_and_follow_to_cart()

    carts_page.assert_main_word_and_result(carts_page.get_main_word(carts_page.main_word), 'Корзина')
    print('Мы в корзине!')
    carts_page.get_screenshot()

    assert carts_page.get_name_of_the_item_in_cart() == name_on_gadget_page
    print('Проверка на совпадение имен пройдена!')

    price = carts_page.get_price_of_the_item_in_cart()
    assert price == price_on_gadget_page
    print('Цены одинаковые!')

def test_user_can_deal_with_filters(browser: WebDriver, gadgets_page: GadgetsPage):

    gadgets_page.visit('https://upstore24.ru/collection/gadgets')

    gadgets_page.select_filters()
    time.sleep(3)
    gadgets_page.check_the_list_is_ascending()


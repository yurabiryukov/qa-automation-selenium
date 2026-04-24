import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.carts_page import CartsPage
from pages.gadgets_page import GadgetsPage


@allure.description("Test info in carts is correct")
def test_info_in_carts_is_correct(browser_with_added_item_in_cart: WebDriver, gadgets_page: GadgetsPage, carts_page_with_items_in_it: CartsPage):

    carts_page_with_items_in_it.select_add_one_more_item_btn()
    assert carts_page_with_items_in_it.get_amount_of_item() == carts_page_with_items_in_it.amount_of_item_via_backend_logic
    print('Было увеличено число товара еще на один')
    carts_page_with_items_in_it.get_price_of_the_item_in_cart_after_increasing_amount()
    print('Цена увеличилась вдвое')

    carts_page_with_items_in_it.select_item_delete_btn()
    assert carts_page_with_items_in_it.get_empty_cart_text_after_deleting_item().text == 'В вашей корзине пока пусто'
    print('Корзина была очищена!')
    carts_page_with_items_in_it.get_screenshot()
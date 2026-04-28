import allure, pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.gadgets_page import GadgetsPage
from pages.order_page import OrderPage


@pytest.mark.smoke
@allure.description("Test user can make order")
def test_user_can_make_order(browser: WebDriver, gadgets_page: GadgetsPage, order_page: OrderPage):

    gadgets_page.visit('https://upstore24.ru/collection/gadgets')

    gadgets_page.select_item_and_follow_to_order_page()
    order_page.assert_main_word_and_result(order_page.get_main_word(order_page.main_word), 'Уже покупали у нас?')
    print('Мы на странице оформления заказа!')

    order_page.check_fill_the_inputs_form(name='Игорь', phone='78888888888')
    assert order_page.get_name_input().get_attribute('value') == 'Игорь'
    assert order_page.get_phone_input().get_attribute('value') == '+7(888)888-88-88'

    order_page.check_create_order_button_is_clickable()
    print('Кнопка "Подтвердить заказ" доступна')

    order_page.check_is_total_price_correct(is_delivery=False)
    print('Итоговая стоимость корректна')

    order_page.check_personal_data_checkbox_is_clickable()
    print('Чекбокс с персональными данными нажат')
    order_page.get_screenshot()
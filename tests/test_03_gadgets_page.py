import time, allure
from pages.gadgets_page import GadgetsPage
from pages.carts_page import CartsPage
from pages.order_page import OrderPage


allure.description("Test guest can follow the whole purchase root")
def test_guest_can_follow_the_whole_purchase_root(browser):
    """
    В данном тесте мы задаем сортировку по скидке товаров во вкладке 'Гаджеты',
    добавляем товар в корзину, проверяем во вкладке 'Корзина' по названию и стоимости товара,
    что добавился именно тот товар, что мы выбирали в 'Гаджеты'. Увеличиваем его количество на 1.
    Проверяем, что стоимость увеличилась x2. Переходим на страницу оформления заказа. Проверяем,
    произошел ли переход, через сравнение атрибута main_word экземпляра класса op
    и фразы 'Уже покупали у нас?' в методе assert_main_word_and_result.
    Заполняем поля с именем и телефоном. Проверяем, что данные совпали.
    Возвращаемся на предыдущую страницу. Чистим корзину. Сохраняем скриншоты.
    """
    link = 'https://upstore24.ru/collection/gadgets'
    browser.get(link)
    browser.maximize_window()

    gp = GadgetsPage(browser)
    gp.select_open_window_close_btn()
    gp.select_filters()
    time.sleep(3)
    # Сохраняем наименование и стоимость товара со страницы с гаджетами для сравнения с корзиной
    name_on_gadget_page = gp.get_item_name()
    price_on_gadget_page = gp.get_item_price()
    gp.select_item()

    cp = CartsPage(browser)
    cp.assert_main_word_and_result(cp.get_main_word(cp.main_word), 'Корзина')
    print('Мы в корзине!')
    cp.get_screenshot()

    assert cp.get_name_of_the_item_in_cart() == name_on_gadget_page
    print('Проверка на совпадение имен пройдена!')

    price = cp.get_price_of_the_item_in_cart()
    assert price == price_on_gadget_page
    print('Цены одинаковые!')

    cp.select_add_one_more_item_btn()
    assert cp.get_amount_of_item() == '2'
    print('Было увеличено число товара еще на один')
    cp.get_price_of_the_item_in_cart_after_increasing_amount()
    print('Цена увеличилась вдвое')
    cp.select_place_an_order_btn()

    op = OrderPage(browser)
    op.assert_main_word_and_result(op.get_main_word(op.main_word), 'Уже покупали у нас?')
    print('Мы на странице оформления заказа!')
    op.fill_the_inputs()
    assert op.get_name_input().get_attribute('value') == 'Игорь'
    assert op.get_phone_input().get_attribute('value') == '+7(888)888-88-88'
    print(f"Указали имя: {op.get_name_input().get_attribute('value')}")
    print(f"Указали номер телефона: {op.get_phone_input().get_attribute('value')}")
    op.get_screenshot()
    op.driver.back()

    cp.select_item_delete_btn()
    assert cp.get_empty_cart_text_after_deleting_item().text == 'В вашей корзине пока пусто'
    print('Корзина была очищена!')
    cp.get_screenshot()

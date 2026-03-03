import allure
from pages.catalog_page import CatalogPage
from pages.gadgets_page import GadgetsPage


@allure.description("Test guest can get in gadgets page")
def test_guest_can_get_in_gadgets_page(browser):
    """
    В данном тесте происходит нажатие на вкладку 'Гаджеты' после того,
    как оказались во вкладке 'Каталог', далее проверка, произошел ли переход,
    через сравнение атрибута main_word экземпляра класса gp и слова 'Гаджеты'
    в методе assert_main_word_and_result.
    Если тест проходит assert, то выводится принт в консоль и сохраняется скриншот.
    """
    link = 'https://upstore24.ru/collection/all'
    browser.get(link)
    browser.maximize_window()

    cp = CatalogPage(browser)
    cp.select_open_window_close_btn()
    cp.select_gadgets_btn()

    gp = GadgetsPage(browser)
    gp.assert_main_word_and_result(gp.get_main_word(gp.main_word), 'Гаджеты')
    print('Мы на странице с гаджетами!')
    gp.get_screenshot()
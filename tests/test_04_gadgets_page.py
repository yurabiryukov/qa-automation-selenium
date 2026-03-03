import time, allure, pytest
from pages.gadgets_page import GadgetsPage


@pytest.mark.parametrize("brand, color, brand_locator, color_locator", GadgetsPage.get_test_params())
@allure.description("Test guest can deal with filters")
def test_guest_can_deal_with_filters(browser, brand, color, brand_locator, color_locator):
    """В данном тесте проверяется работа фильтров: цена, бренд, цвет."""
    link = 'https://upstore24.ru/collection/gadgets'
    browser.get(link)
    browser.maximize_window()

    gp = GadgetsPage(browser)
    gp.select_open_window_close_btn()
    gp.select_filters()
    time.sleep(3)
    gp.check_the_list_is_ascending()
    gp.get_screenshot()

    gp.select_checkbox_filters(brand_locator, color_locator)
    time.sleep(3)
    gp.check_filters_work_as_expected(brand, color)
    gp.get_screenshot()
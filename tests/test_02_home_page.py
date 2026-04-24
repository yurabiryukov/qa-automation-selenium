import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.catalog_page import CatalogPage


@allure.description("Test guest can get in catalog page")
def test_guest_can_get_in_catalog_page(
        browser: WebDriver,
        auth_page: AuthPage,
        home_page: HomePage,
        catalog_page: CatalogPage
):

    home_page.visit('https://upstore24.ru/')
    home_page.select_catalog_btn()

    catalog_page.assert_main_word_and_result(catalog_page.get_main_word(catalog_page.main_word), 'Каталог')
    print('Мы на странице каталога!')





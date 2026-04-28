import pytest
from pages.auth_page import AuthPage
from pages.carts_page import CartsPage
from pages.catalog_page import CatalogPage
from pages.gadgets_page import GadgetsPage
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture
def auth_page(fresh_browser):
    return AuthPage(fresh_browser)

@pytest.fixture
def home_page(fresh_browser):
    return HomePage(fresh_browser)

@pytest.fixture
def catalog_page(browser):
    return CatalogPage(browser)

@pytest.fixture
def order_page(browser):
    return OrderPage(browser)

@pytest.fixture
def gadgets_page(browser):
    return GadgetsPage(browser)

@pytest.fixture
def carts_page(browser):
    return CartsPage(browser)

@pytest.fixture
def carts_page_with_items_in_it(browser_with_added_item_in_cart):
    return CartsPage(browser_with_added_item_in_cart)
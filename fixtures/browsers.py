import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def browser():
    """Фикстура для инициализации браузера Chrome."""
    options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def browser_with_added_item_in_cart(browser):
    """Фикстура для инициализации браузера Chrome для добавления товара в корзину."""
    driver = browser

    driver.get('https://upstore24.ru/collection/gadgets')
    driver.maximize_window()

    item_add_to_cart_locator = "//div[contains(@class, 'col-lg-4')][3]//button[contains(@class, 'button--empty--inverse')]"
    open_the_cart_locator = "//a[@class='button button--primary button--block button--large']"

    item_add_to_cart_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, item_add_to_cart_locator)))
    item_add_to_cart_button.click()

    open_the_cart_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, open_the_cart_locator)))
    open_the_cart_button.click()

    yield driver
    driver.quit()
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BasePage


class HomePage(BasePage):
    """
    Класс домашней страницы.

    Методы разделены по типам:
    - get_* - находят элементы
    - click_* - совершают клики
    - select_* - выполняют последовательности действий

    В тестах используются только select_* методы.
    """
    catalog_btn = "//li[@class='nav-item js-nav-item']//a[text()='Каталог']"

    def get_catalog_btn(self):
        """Находит и возвращает элемент кнопки 'Каталог'."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_btn)))

    def click_catalog_btn(self):
        """Кликает по кнопке 'Каталог'."""
        self.get_catalog_btn().click()

    def select_catalog_btn(self):
        """Основной метод для использования в тестах - открывает каталог."""
        with allure.step("Select catalog btn"):
            self.click_catalog_btn()

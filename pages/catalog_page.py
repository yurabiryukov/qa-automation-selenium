from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):
    """
    Класс страницы каталога.

    Методы разделены по типам:
    - get_* - находят элементы
    - click_* - совершают клики
    - select_* - выполняют последовательности действий

    В тестах используются только select_* методы.
    """
    main_word = "//h1[@class='section-title']"
    gadgets_icon = "//div[contains(@class, 'col-lg-2')][10]//img[contains(@class, 'loaded')]"

    def get_gadgets(self):
        """Находит и возвращает элемент кнопки 'Гаджеты'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.gadgets_icon)))

    def click_gadgets_icon(self):
        """Кликает по кнопке 'Гаджеты'."""
        self.get_gadgets().click()

    def select_gadgets_btn(self):
        """Основной метод для использования в тестах - открывает вкладку 'Гаджеты'."""
        self.click_gadgets_icon()

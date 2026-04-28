import allure
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
    - fill_* - заполнение поля/полей инпут
    - check_* - проверки

    В тестах используются select_*, fill_*, check_* методы.
    """
    main_word = "//h1[@class='section-title']"
    gadgets_icon = "//div[contains(@class, 'col-lg-2')][10]//img[contains(@class, 'loaded')]"
    search_field = "//input[contains(@class, 'js-search-input')]"
    elements_in_search_suggestions = "//span[@class='autocomplete-suggestion-title']"
    no_products_text = "//div[@class='autocomplete-no-suggestion']//div[contains(@class, 'popup--empty')]"

    def get_gadgets(self):
        """Находит и возвращает элемент кнопки 'Гаджеты'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.gadgets_icon)))

    def get_search_field(self):
        """Находит и возвращает элемент поля поиска товаров."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_elements_in_search_suggestions(self):
        """Находит и возвращает результат поиска товаров."""
        return self.driver.find_elements(By.XPATH, self.elements_in_search_suggestions)

    def get_no_products_result(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.XPATH, self.no_products_text), 'По вашему запросу ничего не найдено'))

    def click_gadgets_icon(self):
        """Кликает по кнопке 'Гаджеты'."""
        self.get_gadgets().click()

    def click_search_field(self):
        """Кликает по полю поиска товаров."""
        self.get_search_field().click()

    def remove_value_in_search(self):
        """Очистка поля поиска."""
        self.get_search_field().clear()

    def select_gadgets_btn(self):
        """Открывает вкладку 'Гаджеты'."""
        with allure.step("Select gadgets button"):
            self.click_gadgets_icon()

    def fill_search_field(self, product_name):
        """Производит поиск товара."""
        with allure.step("Fill search field"):
            self.click_search_field()
            self.remove_value_in_search()
            self.get_search_field().send_keys(product_name)

    def check_search_works_as_expected(self, product_name):
        """Проверка результатов поиска."""
        try:
            elements = self.get_elements_in_search_suggestions()
            elements_title = [title.text for title in elements]

            if len(product_name.strip()) != 0 and len(elements_title) != 0:
                return all([product_name.strip() in title for title in elements_title])
            elif len(product_name.strip()) != 0 and len(elements_title) == 0:
                return self.get_no_products_result()
        except Exception:
            self.get_no_products_result()


import allure
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GadgetsPage(BasePage):
    """
    Класс страницы гаджетов.

    Методы разделены по типам:
    - get_* - находят элементы
    - click_* - совершают клики
    - select_* - выполняют последовательности действий

    В тестах используются только select_* методы.
    """
    main_word = "//h1[text()='Гаджеты']"
    filters_btn = "//select[@class='js-filter-sort input--sort']"
    discounts_btn_inside_filter_btn = "//option[@value='descending_discount']"
    item_add_to_cart_btn = "//div[contains(@class, 'col-lg-4')][3]//button[contains(@class, 'button--empty--inverse')]"
    open_the_cart = "//a[@class='button button--primary button--block button--large']"
    item_name = "//div[@class='col-6 col-sm-6 col-md-4 col-lg-4'][3]//div[@class='product_card-title']//a"
    item_price = "//div[contains(@class, 'col-lg-4')][3]//span[contains(@class, 'product_card-price--sale')]"

    def get_filters_btn(self):
        """Находит и возвращает элемент кнопки с фильтрами."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filters_btn)))

    def get_item_name(self):
        """Находит и возвращает наименование 3-го элемента по счету во вкладке 'Гаджеты'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.item_name))).text

    def get_item_price(self):
        """Находит и возвращает стоимость 3-го элемента по счету во вкладке 'Гаджеты'."""
        price_on_website = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.item_price))).text
        price = int(''.join(price_on_website.strip('₽').split(' ')))
        return price

    def get_open_the_cart(self):
        """Находит и возвращает элемент кнопки 'Открыть корзину'."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_the_cart)))

    def get_item_add_to_cart_btn(self):
        """Находит и возвращает элемент кнопки 'Открыть корзину'."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_add_to_cart_btn)))

    def get_discounts_btn_inside_filter_btn(self):
        """Находит кнопку фильтра 'По скидке' в выпадающем списке."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discounts_btn_inside_filter_btn)))

    def click_filters_btn(self):
        """Кликает по кнопке с фильтрами."""
        self.get_filters_btn().click()

    def click_open_the_cart(self):
        """Кликает по кнопке 'Открыть корзину'."""
        self.get_open_the_cart().click()

    def click_item_add_to_cart_btn(self):
        """Кликает по кнопке 'В корзину'."""
        self.get_item_add_to_cart_btn().click()

    def click_discounts_btn_inside_filter_btn(self):
        """Кликает по кнопке 'По скидке' в выпадающем списке."""
        self.get_discounts_btn_inside_filter_btn().click()

    def select_filters(self):
        """
        Основной метод для использования в тестах - открывает вкладку с фильтрами
        и выбирает сортировку 'по скидке'.
        """
        with allure.step("Select filters"):
            self.click_filters_btn()
            self.click_discounts_btn_inside_filter_btn()

    def select_item(self):
        """
        Основной метод для использования в тестах - выбирает товар,
        нажимает на кнопки 'В корзину' и 'Открыть корзину'.
        """
        with allure.step("Select item"):
            self.click_item_add_to_cart_btn()
            self.click_open_the_cart()
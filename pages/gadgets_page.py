import allure, random
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
    - check_* - проверки на применение фильтров
    - select_* - выполняют последовательности действий

    В тестах используются select_* и check_* методы.
    """

    item_number = random.randint(1, 30)
    main_word = "//h1[text()='Гаджеты']"
    filters_btn = "//select[@class='js-filter-sort input--sort']"
    ascending_price_btn_inside_filter_btn = "//option[@value='price']"
    item_add_to_cart_btn = f"//div[contains(@class, 'col-lg-4')][{item_number}]//button[contains(@class, 'button--empty--inverse')]"
    open_the_cart = "//a[@class='button button--primary button--block button--large']"
    item_name = f"//div[@class='col-6 col-sm-6 col-md-4 col-lg-4'][{item_number}]//div[@class='product_card-title']//a"
    item_price = f"//div[contains(@class, 'col-lg-4')][{item_number}]//span[contains(@class, 'product_card-price')]"
    all_products_prices = "//span[contains(@class, 'product_card-price')]"
    all_products_names = "//div[@class='product_card-title']"
    make_an_order_btn = "//a[@class='button button--secondary button--block button--large']"

    def get_filters_btn(self):
        """Находит и возвращает элемент кнопки с фильтрами."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filters_btn)))

    def get_item_name(self):
        """Находит и возвращает наименование 3-го элемента по счету во вкладке 'Гаджеты'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.item_name))).text

    def get_all_products_prices(self):
        """Находит и возвращает цены всех 30 гаджетов во вкладке 'Гаджеты'."""
        return self.driver.find_elements(By.XPATH, self.all_products_prices)

    def get_all_products_names(self):
        """Находит и возвращает наименования всех гаджетов во вкладке 'Гаджеты'."""
        return self.driver.find_elements(By.XPATH, self.all_products_names)

    def get_item_price(self):
        """Находит и возвращает стоимость 3-го элемента по счету во вкладке 'Гаджеты'."""
        price_on_website = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.item_price))).text
        price = int(''.join(price_on_website.strip('₽').split(' ')))
        return price

    def get_open_the_cart(self):
        """Находит и возвращает элемент кнопки 'Открыть корзину'."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_the_cart)))

    def get_item_add_to_cart_btn(self):
        """Находит и возвращает элемент кнопки добавить в корзину."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_add_to_cart_btn)))

    def get_make_an_order_btn(self):
        """Находит и возвращает элемент кнопки оформить заказ."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.make_an_order_btn)))

    def get_ascending_price_btn_inside_filter_btn(self):
        """Находит кнопку фильтра 'Возрастанию цены' в выпадающем списке."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ascending_price_btn_inside_filter_btn)))

    def click_filters_btn(self):
        """Кликает по кнопке с фильтрами."""
        self.get_filters_btn().click()

    def click_open_the_cart(self):
        """Кликает по кнопке 'Открыть корзину'."""
        self.get_open_the_cart().click()

    def click_make_an_order(self):
        """Кликает по кнопке 'Оформить заказ'."""
        self.get_make_an_order_btn().click()

    def click_item_add_to_cart_btn(self):
        """Кликает по кнопке 'В корзину'."""
        self.get_item_add_to_cart_btn().click()

    def click_ascending_price_btn_inside_filter_btn(self):
        """Кликает по кнопке 'Возрастанию цены' в выпадающем списке."""
        self.get_ascending_price_btn_inside_filter_btn().click()

    def select_item_and_follow_to_cart(self):
        """
        Основной метод для использования в тестах - выбирает товар,
        нажимает на кнопки 'В корзину' и 'Открыть корзину'.
        """
        with allure.step("Select item and follow to cart"):
            self.click_item_add_to_cart_btn()
            self.click_open_the_cart()

    def select_item_and_follow_to_order_page(self):
        """
        Основной метод для использования в тестах - выбирает товар,
        нажимает на кнопки 'В корзину' и 'Оформить заказ'.
        """
        with allure.step("Select item and follow to order page"):
            self.click_item_add_to_cart_btn()
            self.click_make_an_order()

    def select_filters(self):
        """
        Основной метод для использования в тестах - выбирает сортировку по возрастанию цены.
        """
        with allure.step("Select item and follow to order page"):
            self.click_filters_btn()
            self.click_ascending_price_btn_inside_filter_btn()

    def check_the_list_is_ascending(self):
        """Проверка, что все цены в списке первых 30 товаров действительно по возрастанию."""
        prices = self.get_all_products_prices()
        list_of_prices = [int(price.text.replace(' ', '').replace('₽', '').strip()) for price in prices]
        n = 0
        for price in list_of_prices:
            if price > n:
                n = price
        assert n == list_of_prices[-1], 'Фильтр не работает'
        print("Фильтр цены по 'По возрастанию' отработал корректно")

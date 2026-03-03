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
    - check_* - проверки на применение фильтров
    - select_* - выполняют последовательности действий

    В тестах используются select_* и check_* методы.
    """
    main_word = "//h1[text()='Гаджеты']"
    filters_btn = "//select[@class='js-filter-sort input--sort']"
    ascending_price_btn_inside_filter_btn = "//option[@value='price']"
    item_add_to_cart_btn = "//div[contains(@class, 'col-lg-4')][3]//button[contains(@class, 'button--empty--inverse')]"
    open_the_cart = "//a[@class='button button--primary button--block button--large']"
    item_name = "//div[@class='col-6 col-sm-6 col-md-4 col-lg-4'][3]//div[@class='product_card-title']//a"
    item_price = "//div[contains(@class, 'col-lg-4')][3]//span[contains(@class, 'product_card-price')]"
    all_products_prices = "//span[contains(@class, 'product_card-price')]"
    all_products_names = "//div[@class='product_card-title']"
    filters_checkbox_locators = {
        'brand': {
            'Apple': "//label[text()='Apple']",
            'Dyson': "//label[text()='Dyson']",
            'Dreame': "//label[text()='Dreame']"
        },
        'color': {
            ('Белый', 'White'): "//label[text()='Белый']",
            ('Черный', 'Black'): "//label[text()='Черный']",
            ('Никель / Медный', 'Nickel / Copper'): "//label[text()='Никель / Медный']"
        }
    }

    @classmethod
    def get_test_params(cls):
        return [(brand_name, color_tuple, brand_locator, color_locator)
                for brand_name, brand_locator in cls.filters_checkbox_locators['brand'].items()
                for color_tuple, color_locator in cls.filters_checkbox_locators['color'].items()]

    def get_brand_color_filters(self, brand, color):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, brand))), WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, color)))

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

    def get_ascending_price_btn_inside_filter_btn(self):
        """Находит кнопку фильтра 'Возрастанию цены' в выпадающем списке."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ascending_price_btn_inside_filter_btn)))

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

    def check_filters_work_as_expected(self, brand, color):
        """Проверка, что все товары после применения фильтров соответствуют фильтрам."""
        names = self.get_all_products_names()
        assert len(names) > 0, f'Нет товаров после применения фильтров: бренд - {brand}, цвет - {color}'
        list_of_names = [name.text for name in names]
        for name in list_of_names:
            flag = False
            assert brand in name, f'Наименование товара не содержит выбранный бренд - {brand}'
            for c in color:
                if c in name:
                    flag = True
            assert flag, f'Наименование товара не содержит выбранный цвет - {color}'
        print(f"По фильтру: бренд - {brand}, цвет - {color} количество товаров - {len(names)}")

    def click_filters_btn(self):
        """Кликает по кнопке с фильтрами."""
        self.get_filters_btn().click()

    def click_brand_color_filters(self, brand, color):
        """Кликает по чекбоксам с фильтрами."""
        self.get_brand_color_filters(brand, color)[0].click()
        self.get_brand_color_filters(brand, color)[1].click()

    def click_open_the_cart(self):
        """Кликает по кнопке 'Открыть корзину'."""
        self.get_open_the_cart().click()

    def click_item_add_to_cart_btn(self):
        """Кликает по кнопке 'В корзину'."""
        self.get_item_add_to_cart_btn().click()

    def click_ascending_price_btn_inside_filter_btn(self):
        """Кликает по кнопке 'Возрастанию цены' в выпадающем списке."""
        self.get_ascending_price_btn_inside_filter_btn().click()

    def select_filters(self):
        """
        Основной метод для использования в тестах - открывает вкладку с фильтрами
        и выбирает сортировку 'Возрастанию цены'.
        """
        with allure.step("Select filters"):
            self.click_filters_btn()
            self.click_ascending_price_btn_inside_filter_btn()

    def select_checkbox_filters(self, brand_locator, color_locator):
        """
        Основной метод для использования в тестах - применяет фильтры по бренду и цвету товара.
        """
        with allure.step("Select checkbox filters"):
            self.click_brand_color_filters(brand_locator, color_locator)

    def select_item(self):
        """
        Основной метод для использования в тестах - выбирает товар,
        нажимает на кнопки 'В корзину' и 'Открыть корзину'.
        """
        with allure.step("Select item"):
            self.click_item_add_to_cart_btn()
            self.click_open_the_cart()
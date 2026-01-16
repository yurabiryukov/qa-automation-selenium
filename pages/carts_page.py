from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BasePage


class CartsPage(BasePage):
    """
    Класс страницы корзины.

    Методы разделены по типам:
    - get_* - находят элементы
    - click_* - совершают клики
    - select_* - выполняют последовательности действий

    В тестах используются только select_* методы.
    """
    main_word = "//h1[text()='Корзина']"
    name_of_the_item_in_cart = "//div[@class='cart-item-title']//a"
    price_of_the_item_in_cart = "//span[contains(@class, 'js-cart-order-total_price')]"
    add_one_more_item_btn = "//div[@class='col col-auto'][2]//button[contains(@class, 'button--medium')]"
    amount_of_item = "//input[@class='input input--counter input--medium']"
    item_delete_btn = "//button[@class='button button--empty button--icon button--medium button--remove']"
    empty_cart_text_after_deleting_item = "//div[contains(@class, 'insales-section-cart')]//div[contains(@class, 'text-center')]"
    place_an_order_btn = "//input[@value='Оформить заказ']"

    def get_empty_cart_text_after_deleting_item(self):
        """Находит и возвращает элемент с надписью, что корзина пуста."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.empty_cart_text_after_deleting_item)))

    def get_item_delete_btn(self):
        """Находит и возвращает элемент удаления позиции с корзины."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.item_delete_btn)))

    def get_name_of_the_item_in_cart(self):
        """Находит и возвращает наименование элемента в корзине."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.name_of_the_item_in_cart))).text

    def get_price_of_the_item_in_cart(self):
        """Находит и возвращает стоимость элемента в корзине."""
        price_on_website = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.price_of_the_item_in_cart))).text
        price = int(''.join(price_on_website.strip('₽').split(' ')))
        return price

    def get_price_of_the_item_in_cart_after_increasing_amount(self):
        """Находит и возвращает стоимость элемента в корзине после увеличения количества товара."""
        new_price = self.get_price_of_the_item_in_cart() * 2
        if new_price < 100000:
            new_price_as_str = str(new_price)[:2] + ' ' + str(new_price)[2:] + ' ₽'
        elif 100000 <= new_price < 1000000:
            new_price_as_str = str(new_price)[:3] + ' ' + str(new_price)[3:] + ' ₽'

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.XPATH, self.price_of_the_item_in_cart), new_price_as_str))

    def get_add_one_more_item_btn(self):
        """Находит и возвращает элемент кнопки увеличения числа товара на 1."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.add_one_more_item_btn)))

    def get_amount_of_item(self):
        """Находит и возвращает количество товара в корзине."""
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.amount_of_item)))
        return element.get_attribute('value')

    def get_place_an_order_btn(self):
        """Находит и возвращает элемент кнопки 'Оформить заказ'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.place_an_order_btn)))

    def click_add_one_more_item_btn(self):
        """Кликает по кнопке увеличения числа товара."""
        self.get_add_one_more_item_btn().click()

    def click_item_delete_btn(self):
        """Кликает по кнопке удаления товара."""
        self.get_item_delete_btn().click()

    def click_place_an_order_btn(self):
        """Кликает по кнопке 'Оформить заказ'."""
        self.get_place_an_order_btn().click()

    def select_add_one_more_item_btn(self):
        """
        Основной метод для использования в тестах - нажимает кнопку
        увеличения числа товара.
        """
        self.click_add_one_more_item_btn()

    def select_item_delete_btn(self):
        """
        Основной метод для использования в тестах - нажимает кнопку
        удаления товара.
        """
        self.click_item_delete_btn()

    def select_place_an_order_btn(self):
        """
        Основной метод для использования в тестах - нажимает кнопку
        'Оформить заказ'.
        """
        self.click_place_an_order_btn()


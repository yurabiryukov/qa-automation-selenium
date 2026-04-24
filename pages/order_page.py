import allure
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    """
    Класс страницы каталога.

    Методы разделены по типам:
    - get_* - находят элементы
    - send_keys_* - заполняют поля
    - fill_* - выполняют последовательности действий

    В тестах используется только fill_* метод.
    """

    main_word = "//a[@class='link js-modal-toggler']"
    name_input = "//input[@id='client_contact_name']"
    phone_input = "//input[contains(@class, 'co-input-phone')]"
    create_order_button = "//button[@id='create_order']"
    total_price = "//div[@id='total_price']"
    delivery_price = "//span[@id='price_2654338']"
    shipping_address = "//textarea[@id='shipping_address_address']"
    delivery_button = "//label[@for='order_delivery_variant_id_2654338']"
    all_products_prices = "//div[@class='co-basket_item-total']//span[contains(@class, 'co-price--current')]"
    personal_data_checkbox = "//div[@class='consent_to_personal_data_checkbox co-checkout-block']//span[contains(@class, 'co-toggable_field-input--checkbox')]"

    def get_name_input(self):
        """Находит и возвращает поле с именем во вкладке 'Оформление заказа'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.name_input)))

    def get_total_price(self):
        """Находит и возвращает поле с итоговой стоимостью."""
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.total_price))).text
        return int(element.replace(' ', '').replace('₽', '').strip())

    def get_shipping_address(self):
        """Находит и возвращает поле с адресом."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.shipping_address)))

    def get_personal_data_checkbox(self):
        """Находит и возвращает чекбокс с персональными данными."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_data_checkbox)))

    def get_delivery_button(self):
        """Находит и возвращает кнопку с доставкой."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.delivery_button)))

    def get_delivery_price(self):
        """Находит и возвращает стоимость доставки."""
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.delivery_price))).text
        return int(element.replace(' ', '').replace('₽', '').strip())

    def get_phone_input(self):
        """Находит и возвращает поле с телефоном во вкладке 'Оформление заказа'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.phone_input)))

    def get_create_order_button(self):
        """Находит и возвращает кнопку "Подтвердить заказ"."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_order_button)))

    def get_all_products_prices(self):
        """Находит и возвращает цены всех товаров в заказе."""
        return self.driver.find_elements(By.XPATH, self.all_products_prices)

    def click_delivery_button(self):
        """Нажимает по радиобаттону с доставкой."""
        self.get_delivery_button().click()

    def click_personal_data_checkbox(self):
        """Нажимает по чекбоксу с персональными данными."""
        self.get_personal_data_checkbox().click()

    def send_keys_name_input(self, name):
        """Заполняет поле именем."""
        self.get_name_input().clear()
        self.get_name_input().send_keys(name)

    def send_keys_phone_input(self, phone):
        """Заполняет поле с номером телефона."""
        self.get_phone_input().clear()
        self.get_phone_input().send_keys(phone)

    def check_fill_the_inputs_form(self, name, phone):
        """Основной метод для использования в тестах - заполняет поля с именем и телефоном."""
        with allure.step("Check fill the inputs form"):
            self.send_keys_name_input(name)
            self.send_keys_phone_input(phone)

    def check_create_order_button_is_clickable(self):
        """Основной метод для использования в тестах - проверяет доступность кнопки "Подтвердить заказ"."""
        with allure.step("Check create order button is clickable"):
            self.get_create_order_button()

    def check_is_total_price_correct(self, is_delivery: bool = False):
        if is_delivery:
            self.click_delivery_button()
            prices = self.get_all_products_prices()
            list_of_prices = sum(int(price.text.replace(' ', '').replace('₽', '').strip()) for price in prices)
            delivery_cost = self.get_delivery_price()
            assert list_of_prices + delivery_cost == self.get_total_price()
        else:
            prices = self.get_all_products_prices()
            list_of_prices = sum(int(price.text.replace(' ', '').replace('₽', '').strip()) for price in prices)
            assert list_of_prices == self.get_total_price()

    def check_personal_data_checkbox_is_clickable(self):
        """Основной метод для использования в тестах - проверяет нажатие чекбокса с персональными данными."""
        with allure.step("Check personal data checkbox is clickable"):
            self.click_personal_data_checkbox()





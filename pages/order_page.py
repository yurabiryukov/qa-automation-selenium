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

    def get_name_input(self):
        """Находит и возвращает поле с именем во вкладке 'Оформление заказа'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.name_input)))

    def get_phone_input(self):
        """Находит и возвращает поле с телефоном во вкладке 'Оформление заказа'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.phone_input)))

    def send_keys_name_input(self):
        """Заполняет поле именем."""
        self.get_name_input().clear()
        self.get_name_input().send_keys('Игорь')

    def send_keys_phone_input(self):
        """Заполняет поле с номером телефона."""
        self.get_phone_input().clear()
        self.get_phone_input().send_keys('78888888888')

    def fill_the_inputs(self):
        """Основной метод для использования в тестах - заполняет поля с именем и телефоном."""
        with allure.step("Fill the inputs"):
            self.send_keys_name_input()
            self.send_keys_phone_input()


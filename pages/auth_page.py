import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BasePage


class AuthPage(BasePage):
    """
    Класс страницы авторизации.

    Методы разделены по типам:
    - get_* - находят элементы
    - send_keys_* - заполняют поля
    - click_* - совершают клики
    - fill_* - выполняют последовательности действий

    В тестах используется fill_* метод.
    """
    email_input = "//input[@id='email']"
    password_input = "//input[@id='password']"
    main_word = "//h1[contains(@class, 'co-title--h1')]"
    enter_btn = "//button[contains(@class, 'js-co-login-submit')]"

    def get_email_input(self):
        """Находит и возвращает поле с почтой на странице авторизации."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.email_input)))

    def get_password_input(self):
        """Находит и возвращает поле с паролем на странице авторизации."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.password_input)))

    def get_enter_btn(self):
        """Находит и возвращает кнопку 'Войти'."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.enter_btn)))

    def click_enter_btn(self):
        """Кликает по кнопке "Войти"."""
        self.get_enter_btn().click()

    def send_keys_email_input(self):
        """Заполняет поле с почтой."""
        self.get_email_input().clear()
        self.get_email_input().send_keys('test@test.test')

    def send_keys_password_input(self):
        """Заполняет поле с паролем."""
        self.get_password_input().clear()
        self.get_password_input().send_keys('123456789')

    def fill_the_inputs(self):
        """Основной метод для использования в тестах - заполняет поля с почтой и паролем и нажимает 'Войти'."""
        with allure.step("Fill the inputs"):
            self.send_keys_email_input()
            self.send_keys_password_input()
            self.click_enter_btn()
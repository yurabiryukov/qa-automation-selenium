import datetime, os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс, содержащий универсальные методы"""
    open_window_close_btn = "//jdiv[@class='closeIcon__eiV1K']"
    logo_btn = "//div[contains(@class, 'text-lg-left')]//a[@class='logo']"

    def __init__(self, driver):
        self.driver = driver

    def get_main_word(self, main_word):
        """
        Здесь в main_word передается одноименный атрибут каждого класса страницы,
        далее по этому 'ключевому' слову будет происходить сравнение:
        на ту ли страницу случился переход.
        """
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, main_word))).text

    def get_open_window_close_btn(self):
        """Находит и возвращает элемент кнопки закрытия онлайн чата-поддержки."""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_window_close_btn)))

    def get_logo_btn(self):
        """Находит и возвращает кнопку лого."""
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.logo_btn)))

    def click_logo_btn(self):
        """Кликает по кнопке лого."""
        self.get_logo_btn().click()

    def select_open_window_close_btn(self, timeout=30):
        """
        Основной метод для использования в тестах - закрывает окно с чатом-поддержки, если
        мы заходим на сайт в рабочее время поддержки (с 10 до 20:30 мск),
        либо продолжает работу скрипта без закрытия окна.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.open_window_close_btn))).click()
            print("Окно чата закрыто")
        except TimeoutException:
            print(f"Окно чата не появилось за {timeout} сек (возможно, нерабочее время поддержки)")

    def assert_main_word_and_result(self, main_word, result):
        """
        В main_word будет одноименный атрибут каждого класса, в result - строка - какое-то слово
        или фраза с той страницы, на которую произошел переход.
        """
        assert main_word == result

    def get_screenshot(self):
        """Сохраняет скриншот"""
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        test_file = os.path.basename(sys._getframe().f_back.f_code.co_filename)
        test_filename = os.path.splitext(test_file)[0]
        screenshot_name = f"{test_filename} {now_date}.png"
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshots_dir = os.path.join(project_root, "screenshots")
        full_path = os.path.join(screenshots_dir, screenshot_name)
        self.driver.save_screenshot(full_path)

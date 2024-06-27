from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.main_page_locators as locators
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент')
    def find_element_with_wait(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                locator))
        self.driver.find_element(*locator).click()

    @allure.step('Вводим текст')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    @allure.step('Прокручиваем страницу до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем на кнопку принятия cookies')
    def accept_cookies(self):
        self.click_to_element(locators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Переключаемся на другую вкладку')
    def change_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

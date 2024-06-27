from pages.base_page import BasePage
import locators.main_page_locators as locators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим к форме заказа')
    def go_to_order_page(self):
        self.click_to_element(locators.HEADER_ORDER_BUTTON)

    @allure.step('Получаем текст ответа по порядковому номеру вопроса')
    def get_answer_text(self, num):
        locator_question_formatted = self.format_locator(locators.QUESTION, num)
        locator_answer_formatted = self.format_locator(locators.ANSWER, num)
        self.scroll_to_element(locator_question_formatted)
        self.click_to_element(locator_question_formatted)
        return self.get_text_from_element(locator_answer_formatted)

    @allure.step('Открываем форму заказа по кнопке вверху страницы')
    def open_person_info_form_by_header_button(self):
        self.click_to_element(locators.HEADER_ORDER_BUTTON)

    @allure.step('Открываем форму заказа по кнопке внизу страницы')
    def open_person_info_form_by_content_button(self):
        self.scroll_to_element(locators.CONTENT_ORDER_BUTTON)
        self.click_to_element(locators.CONTENT_ORDER_BUTTON)

from pages.base_page import BasePage
import locators.transition_page_locators as locators
import locators.main_page_locators as main_page_locators
import allure


class TransitionPage(BasePage):

    @allure.step('Переходим на главную страницу, кликая на логотип "Самоката"')
    def go_to_main_page_by_scooter_logo(self):
        self.click_to_element(locators.SCOOTER_LOGO)

    @allure.step('Получаем текст заголовка на главной странице')
    def get_main_page_header_text(self):
        return self.find_element_with_wait(main_page_locators.HOME_PAGE_HEADER).text

    @allure.step('Переходим на "Дзен", кликая на логотип "Яндекс"')
    def go_to_dzen_by_yandex_logo(self):
        self.click_to_element(locators.YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получаем заголовок раздела новости со страницы "Дзен"')
    def get_dzen_news_title(self):
        return self.find_element_with_wait(locators.DZEN_NEWS_TITLE, timeout=10).text

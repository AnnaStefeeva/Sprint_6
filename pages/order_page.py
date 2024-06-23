from pages.base_page import BasePage
import locators.order_page_locators as locators
import allure


class OrderPage(BasePage):

    @allure.step('Ожидаем появления формы "Для кого самокат"')
    def wait_person_info_form(self):
        self.find_element_with_wait(locators.PERSON_INFO_FORM)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, station_name):
        self.click_to_element(locators.PersonForm.METRO_STATION)
        self.find_element_with_wait(locators.PersonForm.METRO_STATION_LIST)
        station_button_locator = (
            locators.PersonForm.METRO_STATION_BUTTON[0],
            locators.PersonForm.METRO_STATION_BUTTON[1].format(station_name)
        )
        self.click_to_element(station_button_locator)

    @allure.step('Выбираем период аренды')
    def select_order_period(self, rent_period):
        self.click_to_element(locators.RentForm.PERIOD)
        item_locator = self.format_locator(locators.RentForm.PERIOD_ITEM, rent_period)
        self.click_to_element(item_locator)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_person_info_form(self, person_info):
        self.add_text_to_element(locators.PersonForm.FIRST_NAME, person_info['first_name'])
        self.add_text_to_element(locators.PersonForm.SECOND_NAME, person_info['last_name'])
        self.add_text_to_element(locators.PersonForm.ADDRESS, person_info['address'])
        self.add_text_to_element(locators.PersonForm.PHONE, person_info['phone_number'])
        self.select_metro_station(person_info['metro_station'])
        self.click_to_element(locators.PersonForm.NEXT_BUTTON)

    @allure.step('Заполняем форму "Про аренду"')
    def fill_rent_info_form(self, rent_info):
        self.add_text_to_element(locators.RentForm.START_DATE, rent_info['start_date'])
        self.select_order_period(rent_info['rent_period'])
        self.add_text_to_element(locators.RentForm.COMMENTS, rent_info['comment'])
        if rent_info['color'] == 'black':
            self.click_to_element(locators.RentForm.BLACK_COLOR_OF_SCOOTER)
        else:
            self.click_to_element(locators.RentForm.GREY_COLOR_OF_SCOOTER)

from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest
import data
import allure


@allure.suite('Тесты страниц заказа')
class TestOrderPage:
    @allure.title('Создание заказа')
    @allure.description('Кликаем на кнопку «Заказать» вверху страницы, заполняем форму "Для кого самокат", форму '
                        '"Про аренду" и подтверждаем заказ')
    @pytest.mark.parametrize(
        'person_info, rent_info',
        [
            (data.PERSON_1, data.RENT_INFO_1),
            (data.PERSON_2, data.RENT_INFO_2)
        ]
    )
    def test_make_order(self, driver, person_info, rent_info):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.open_person_info_form_by_header_button()

        order_page = OrderPage(driver)
        order_page.wait_person_info_form()
        order_page.fill_person_info_form(person_info)

        rent_info_header = order_page.get_rent_info_header()
        assert rent_info_header.text == data.RENT_INFO_HEADER

        order_page.fill_rent_info_form(rent_info)
        order_page.click_order_finish_button()
        order_page.confirm_order()

        order_finish_header = order_page.get_order_info_header()
        assert data.ORDER_FINISH_HEADER in order_finish_header.text

    @allure.title('Проверка кнопки "Заказать" внизу страницы')
    @allure.description('Кликаем на кнопку «Заказать» внизу страницы, проверяем переход на форму "Для кого самокат"')
    def test_open_order_form_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.open_person_info_form_by_content_button()

        order_page = OrderPage(driver)
        header = order_page.get_person_info_header()
        assert header.text == data.PERSON_INFO_HEADER

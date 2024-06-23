from pages.main_page import MainPage
import pytest
import data
import allure


@allure.title('Тесты главной страницы')
class TestMainPage:

    @allure.title('Проверка соответствия текста ответа вопросу')
    @allure.description('На странице ищем вопрос по его порядковому номеру, кликаем на стрелочку, получаем текст '
                        'ответа и проверяем его соответствие вопросу')
    @pytest.mark.parametrize(
        'num, answer_text',
        [
            (0, data.ANSWER_1),
            (1, data.ANSWER_2),
            (2, data.ANSWER_3),
            (3, data.ANSWER_4),
            (4, data.ANSWER_5),
            (5, data.ANSWER_6),
            (6, data.ANSWER_7),
            (7, data.ANSWER_8)
        ]
    )
    def test_answers_to_questions(self, driver, num, answer_text):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        assert main_page.get_answer_text(num) == answer_text

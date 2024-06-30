from selenium.webdriver.common.by import By


PERSON_INFO_FORM = (By.XPATH, '//div[contains(@class, "Order_Form")]')

PERSON_INFO_HEADER = (By.XPATH, '//div[contains(@class, "Order_Header") and text()="Для кого самокат"]')

RENT_INFO_HEADER = (By.XPATH, '//div[contains(@class, "Order_Header") and text()="Про аренду"]')


class PersonForm:
    FIRST_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    SECOND_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button')
    METRO_STATION_LIST = (By.XPATH, '//div[@class="select-search__select"]')
    METRO_STATION_BUTTON = (By.XPATH, '//button[contains(@class, "select-search__option")]//div[text()="{}"]')


class RentForm:
    START_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    PERIOD = (By.XPATH, '//span[@class="Dropdown-arrow"]')
    BLACK_COLOR_OF_SCOOTER = (By.ID, 'black')
    GREY_COLOR_OF_SCOOTER = (By.ID, 'grey')
    COMMENTS = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    PERIOD_ITEM = (By.XPATH, '//div[contains(@class, "Dropdown-option") and text()="{}"]')
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')


CONFIRMATION_BUTTON = (By.XPATH, '//button[text()="Да"]')

ORDER_FINISH_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]')

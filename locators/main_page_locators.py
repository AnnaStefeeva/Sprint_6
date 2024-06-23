from selenium.webdriver.common.by import By


# Вопрос в разделе "Вопросы о важном"
QUESTION = (By.ID, "accordion__heading-{}")

# Ответ в разделе "Вопросы о важном"
ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']/p")

# Кнопка принятия кукис
ACCEPT_COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

HEADER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')

CONTENT_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')

HOME_PAGE_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header")]')

import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.cart_page import Cart_page


class Client_information_page(Base):
    """Работа со страницей оформления заказа - БЕЗ САМОЙ ОТПРАВКИ!"""

    def __init__(self, driver):
        """Объявление переменной драйвера"""
        super().__init__(driver)
        self.driver = driver

    # Locators

    """блок Данные получателя"""
    first_name = "//input[@name = 'firstName']"
    last_name = "//input[@name = 'lastName']"
    phone_number = "//input[@name = 'phone']"

    """блок Данные Страхователя"""
    first_name_insured = "//input[@name='insurance-form_firstName']"
    last_name_insured = "//input[@name='insurance-form_lastName']"
    phone_number_insured = "//input[@name='insurance-form_phone']"
    email_insured = "//input[@name='insurance-form_email']"
    data_checking_checkbox = "//input[@id='insuranceConfirm']/parent::span/parent::label"

    """блок Получение и оплата"""
    pick_up_point_button = "//button[@class= 'e11203e30 css-suhtla-Button--StyledButton-Button--Button ekx3zbi0']"
    pick_up_point_1 = "(//button[@data-meta-name= 'SelfDeliveryStoresList__select-button'])[1]"
    right_checkbox = "//input[@id='contactPaymentConfirm']/parent::span/parent::label"
    email = "//input[@name = 'email']"

    """Кнопка отправки заказа - НЕ НАЖИМАТЬ"""
    send_order = "//button[@data-meta-name= 'SubmitButton']"

    """Данные для проверки"""
    price_order_product_add_1 = "(//span[@class='e4ahr150 e1a7a4n70 css-1a5t9d8-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0'])[2]"
    name_order_product_1 = "(//span[@class='e1ve2340 e1a7a4n70 css-onywqm-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent ez8h4tf0'])[3]"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_first_name_insured(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_insured)))

    def get_last_name_insured(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_insured)))

    def get_phone_number_insured(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number_insured)))

    def get_email_insured(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_insured)))

    def get_pick_up_point_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_point_button)))

    def get_pick_up_point_1(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_point_1)))

    def get_right_checkbox(self):
        return WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, self.right_checkbox)))

    def get_data_checking_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_checking_checkbox)))
    def get_send_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_order)))

    def get_price_order_product_add_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_order_product_add_1)))

    def get_name_order_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_order_product_1)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print(f"Input first name: {first_name}")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print(f"Input last name: {last_name}")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print(f"Input phone number: {phone_number}")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print(f"Input email: {email}")

    def input_first_name_insured(self, first_name_insured):
        self.get_first_name_insured().send_keys(first_name_insured)
        print(f"Input first name insured: {first_name_insured}")

    def input_last_name_insured(self, last_name_insured):
        self.get_last_name_insured().send_keys(last_name_insured)
        print(f"Input last name insured: {last_name_insured}")

    def input_phone_number_insured(self, phone_number_insured):
        self.get_phone_number_insured().send_keys(phone_number_insured)
        print(f"Input phone number insured: {phone_number_insured}")

    def input_email_insured(self, email_insured):
        self.get_email_insured().send_keys(email_insured)
        print(f"Input email insured: {email_insured}")

    def click_pick_up_point_button(self):
        self.get_pick_up_point_button().click()
        print(f"Click pick_up_point_button")

    def click_pick_up_point_1(self):
        self.get_pick_up_point_1().click()
        print(f"Click pick_up_point_1")

    def click_right_checkbox(self):
        self.get_right_checkbox().click()
        print(f"Click right checkbox")

    def click_data_checking_checkbox(self):
        self.get_data_checking_checkbox().click()
        print(f"Click data checking checkbox")

    # Methods

    def input_information(self):
        """Заполнение клиентской информации"""
        self.get_current_url()

        self.input_first_name("Антонина")
        self.input_last_name('Кудряшко')
        self.input_phone_number('8(978)740-66-44')

        self.input_first_name_insured('Павел')
        self.input_last_name_insured('Кудряшко')
        self.input_phone_number_insured('8(978)740-66-44')
        self.input_email_insured('test@email.ru')
        self.click_data_checking_checkbox()

        self.click_pick_up_point_button()
        self.click_pick_up_point_1()

        self.driver.execute_script("window.scrollTo(0,1400)")
        self.click_right_checkbox()
        self.input_email('email@test.ru')

        self.assert_button_enabled(self.get_send_order())
        self.get_screenshot('order_button')

    def confirm_info_finish_product_1(self, name, price):
        self.assert_word(self.get_name_order_product_1(), name)
        self.assert_word(self.get_price_order_product_add_1(), price)

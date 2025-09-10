from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

from pages.catalog import Catalog

class Cart_page(Base):
    """Работа со страницей корзины"""

    def __init__(self, driver):
        """Объявление переменной драйвера"""
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_cart_product_1 = "(//span[@data-meta-is-total='notTotal'])[1]/child::span[1]"
    price_cart_product_add_1 = "//span[@class='e4ahr150 e1a7a4n70 css-7u7wrk-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0']"
    name_cart_product_1 = "//span[@class='e9qk9yp0 e1a7a4n70 css-nqrmhv-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent ez8h4tf0']/child::span"

    add_kombo_protect_2yo = "(//label[@data-meta-value='+2 года'])[2]"

    checkout_button = "//button[@title= 'Перейти к оформлению']"
    as_guest_button = "//span[contains(text(), 'Продолжить как гость')]"

    header_order = "//span[@class='e9qk9yp0 e1a7a4n70 css-10tq7m6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent ez8h4tf0']"

    # Getters

    def get_price_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_cart_product_1)))

    def get_price_cart_product_add_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_cart_product_add_1)))

    def get_name_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_cart_product_1)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_as_guest_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.as_guest_button)))

    def get_add_kombo_protect_2yo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_kombo_protect_2yo)))

    def get_header_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_order)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print(f"Click checkout button")
    def click_as_guest_button(self):
        self.get_as_guest_button().click()
        print(f"Click as guest button")

    def click_add_kombo_protect_2yo(self):
        self.get_add_kombo_protect_2yo().click()
        print(f"Click add_kombo_protect_2yo")

    # Methods

    def confirm_info_cart_product_1(self):
        ctlg = Catalog(self.driver)
        self.assert_word(ctlg.get_price_product_1(), f'{self.get_price_cart_product_1().text}₽')
        self.assert_word(ctlg.get_name_product_1(), self.get_name_cart_product_1().text)

    def additional_product_service(self):
        self.driver.execute_script("window.scrollTo(0,400)")
        self.click_add_kombo_protect_2yo()

    def product_confirm(self):
        self.click_checkout_button()
        self.click_as_guest_button()

        self.assert_word(self.get_header_order(), "Оформление заказа")
        self.get_screenshot("client_info_page")

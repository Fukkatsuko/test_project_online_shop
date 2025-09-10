import datetime
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base

class Catalog(Base):
    """Работа со страницей Каталога"""


    def __init__(self, driver):
        """Объявление переменной драйвера"""
        super().__init__(driver)
        self.driver = driver

    # Locators

    """Фильтры"""
    min_price = "//input[@name = 'input-min']"
    max_price = "//input[@name = 'input-max']"
    show_all_brands = "(//button[@data-meta-name= 'FilterGroup__show-all'])[2]"
    search_brands = "(//input[@data-meta-name = 'FilterSearch__input'])[2]"
    acer_checkbox = "//input[@id = 'acer']/parent::span/parent::label"
    honor_checkbox = "//input[@id = 'honor']/parent::span/parent::label"
    huawei_checkbox = "//input[@id = 'huawei']/parent::span/parent::label"
    checkbox_512gb = "//input[@id = '18332_3512d1gb']/parent::span/parent::label"
    checkbox_1tb = "//input[@id = '18332_31d1tb']/parent::span/parent::label"
    high_rate = "//button[@name = '4 и выше']"
    apply_button = "//span[contains(text(), 'Применить выбранное')]"

    """Список товаров"""
    rate_sorting = "//button[@data-meta-value='rating']"
    select_product_1 = "(//button[@data-meta-name='Snippet__cart-button'])[1]"
    price_product_1 = "(//span[@data-meta-is-total= 'notTotal'])[1]"
    name_product_1 = "(//a[@data-meta-name= 'Snippet__title'])[1]"

    """Мод. окно добавление товара"""
    header_send_in_cart = "//span[@class='e9qk9yp0 e1a7a4n70 app-catalog-10tq7m6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent ez8h4tf0']"

    """Корзина"""
    cart_button_window = "(//span[contains(text(), 'Перейти в корзину')]/parent::button)[1]"
    cart_button_general = "//a[@href = '/order/']"
    header_cart = "//span[@class='e9qk9yp0 e1a7a4n70 css-13eo1xz-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent ez8h4tf0']"
    price_cart_product_1 = "(//span[@data-meta-is-total= 'notTotal'])[1]"
    name_cart_product_1 = "//span[@class= 'e9qk9yp0 e1a7a4n70 css-nqrmhv-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent ez8h4tf0']/child::span"

    # Getters

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_show_all_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_brands)))

    def get_search_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_brands)))

    def get_acer_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.acer_checkbox)))

    def get_honor_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.honor_checkbox)))

    def get_huawei_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.huawei_checkbox)))

    def get_checkbox_512gb(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_512gb)))

    def get_checkbox_1tb(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_1tb)))

    def get_high_rate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.high_rate)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_rate_sorting(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rate_sorting)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.name_cart_product_1)))

    def get_cart_button_window(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart_button_window)))

    def get_cart_button_general(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart_button_general)))
    def get_header_send_in_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.header_send_in_cart)))

    def get_header_cart(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.header_cart)))

    # Actions

    def input_min_price(self, min_price):
        self.get_min_price().send_keys(Keys.CONTROL + "a")
        self.get_min_price().send_keys(Keys.DELETE)
        self.get_min_price().send_keys(min_price)
        print(f"Input min price: {min_price}")

    def input_max_price(self, max_price):
        self.get_max_price().send_keys(Keys.CONTROL + "a")
        self.get_max_price().send_keys(Keys.DELETE)
        self.get_max_price().send_keys(max_price)
        print(f"Input max price: {max_price}")

    def input_search_brands(self, brand):
        self.get_search_brands().send_keys(brand)
        print(f"Input search brands: {brand}")

    def click_show_all_brands(self):
        self.get_show_all_brands().click()
        print(f"Click show all brands")

    def click_acer_checkbox(self):
        self.get_acer_checkbox().click()
        print(f"Click acer checkbox")

    def click_honor_checkbox(self):
        self.get_honor_checkbox().click()
        print(f"Click honor checkbox")

    def click_huawei_checkbox(self):
        self.get_huawei_checkbox().click()
        print(f"Click huawei checkbox")

    def click_checkbox_512gb(self):
        self.get_checkbox_512gb().click()
        print(f"Click checkbox 512gb")

    def click_checkbox_1tb(self):
        self.get_checkbox_1tb().click()
        print(f"Click checkbox 1tb")

    def click_high_rate(self):
        self.get_high_rate().click()
        print(f"Click high rate")

    def click_apply_button(self):
        self.get_apply_button().click()
        print(f"Click apply button")

    def click_rate_sorting(self):
        self.get_rate_sorting().click()
        print(f"Click rate sorting")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print(f"Click select product 1")

    def click_cart_button_window(self):
        self.get_cart_button_window().click()
        print(f"Click cart button window")

    def click_cart_button_general(self):
        self.get_cart_button_general().click()
        print(f"Click cart button general")

    # Methods

    def select_filters(self):
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера

        actions.move_to_element(self.get_min_price()).perform()  # наведение на требуемые объект страницы, по локатору
        self.input_min_price(30000)
        self.input_max_price(120000)

        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_high_rate()

        self.driver.execute_script("window.scrollTo(0, 800)")
        self.click_show_all_brands()
        self.click_acer_checkbox()

        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.input_search_brands('H')
        self.click_honor_checkbox()
        self.click_huawei_checkbox()

        self.driver.execute_script("window.scrollTo(0, 2200)")
        self.click_checkbox_512gb()
        self.click_checkbox_1tb()

        self.driver.execute_script("window.scrollTo(0, 3500)")
        self.click_apply_button()
        time.sleep(5)

    def select_rate_sorting(self):
        """Выбор сортировки - по рейтингу"""
        self.click_rate_sorting()
        time.sleep(5)

    def select_products_1(self):
        """Выбор продукта"""
        self.driver.execute_script("window.scrollTo(0,500)")
        self.get_current_url()
        self.click_select_product_1()

        try:
            self.assert_word(self.get_header_send_in_cart(), "Товар добавлен в корзину")
            self.get_screenshot('product_is_chosen')
            self.click_cart_button_window()
        except TimeoutException:
            self.click_cart_button_general()

        self.get_current_url()
        self.assert_word(self.get_header_cart(), "Корзина")
        self.get_screenshot('cart')
        print("-------------------------------------")



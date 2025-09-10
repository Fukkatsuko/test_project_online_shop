from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Main_page(Base):
    """Работа с главной страницей"""

    url = 'https://www.citilink.ru/'


    def __init__(self, driver):
        """Объявление переменной драйвера"""
        super().__init__(driver)
        self.driver = driver

    # Locators

    menu_button = "//a[@href = '/catalog/']"
    laptop_pc_menu = "(//a[@href='/catalog/noutbuki-i-kompyutery/?ref=mainmenu'])[2]"
    laptop_menu = "//a[@href='https://www.citilink.ru/catalog/noutbuki/?ref=mainmenu_left']"

    # Getters

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_laptop_pc_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_pc_menu)))

    def get_laptop_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_menu)))

    # Actions

    def click_menu_button(self):
        self.get_menu_button().click()
        print(f"Click menu button")

    def click_laptop_pc_menu(self):
        self.get_laptop_pc_menu().click()
        print(f"Click laptop & pc menu")

    def click_laptop_menu(self):
        self.get_laptop_menu().click()
        print(f"Click laptop menu")

    # Methods

    def goto_laptop_catalog(self):
        """Переход в каталог ноутов"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

        self.click_menu_button()
        self.click_laptop_pc_menu()
        self.click_laptop_menu()

        self.get_current_url()
        self.assert_url('https://www.citilink.ru/catalog/noutbuki/?ref=mainmenu_left')

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.catalog import Catalog
from pages.client_information_page import Client_information_page
from pages.main_page import Main_page

@pytest.mark.run(order = 2)
def test_order_product_rate(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test with rate")

    """Перейти в каталог ноутбуков"""
    mp = Main_page(driver)
    mp.goto_laptop_catalog()

    """Выбрать фильтры и перейти к товарам"""
    ctg = Catalog(driver)
    ctg.select_filters()

    """Установить сортировку по рейтингу и выбрать первый товар"""
    ctg.select_rate_sorting()
    ctg.select_products_1()

    """Проверка товара и работа с корзиной"""
    cart = Cart_page(driver)
    time.sleep(5)
    cart.confirm_info_cart_product_1()
    cart.additional_product_service()

    """Сохранение общей стоимости заказа в корзине"""
    time.sleep(5)
    cart_add_price = cart.get_price_cart_product_add_1().text
    cart_name = cart.get_name_cart_product_1().text
    cart.product_confirm()

    """Заполнение информации пользователя для оформления заказа"""
    info = Client_information_page(driver)
    info.confirm_info_finish_product_1(cart_name, cart_add_price)
    info.input_information()

    print("Finish test with rate")
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order = 1)
def test_order_product_no_rate(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test without rate")

    """Перейти в каталог ноутбуков"""
    mp = Main_page(driver)
    mp.goto_laptop_catalog()

    """Выбрать фильтры и перейти к товарам"""
    ctg = Catalog(driver)
    ctg.select_filters()

    """Выбрать первый товар"""
    ctg.select_products_1()

    """Проверка товара и работа с корзиной"""
    cart = Cart_page(driver)
    time.sleep(5)
    cart.confirm_info_cart_product_1()
    cart.additional_product_service()

    """Сохранение общей стоимости заказа в корзине"""
    time.sleep(5)
    cart_add_price = cart.get_price_cart_product_add_1().text
    cart_name = cart.get_name_cart_product_1().text
    cart.product_confirm()

    """Заполнение информации пользователя для оформления заказа"""
    info = Client_information_page(driver)
    info.confirm_info_finish_product_1(cart_name, cart_add_price)
    info.input_information()

    print("Finish test without rate")
    time.sleep(5)
    driver.quit()
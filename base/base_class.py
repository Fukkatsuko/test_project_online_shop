import datetime


class Base():
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver


    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url: "+ get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        # print(f"{value_word} - {result}")
        assert value_word == result
        print(f"Good value word - {result}")

    """Method screenshot"""
    def get_screenshot(self, name_page):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + name_page + "_" + now_date + '.png'
        self.driver.save_screenshot('D:\\Soft\\PycharmProjects\\test_project_online_shop\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method assert url"""

    def assert_button_enabled(self, button):
        assert button.is_enabled() == True
        print("Отправка заказа возможна!")
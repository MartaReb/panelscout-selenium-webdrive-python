import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    driver = None
    driver_service = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")


class TestMediumPage(unittest.TestCase):

    driver = None
    driver_service = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://medium.com/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def get_page_title(self, url):
        return self.driver.title

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com/')
        expected_title = 'Medium – Where good ideas find you.'
        assert actual_title == expected_title

    @classmethod
    def tearDown(self):
        self.driver.quit()
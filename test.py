from unittest import TestCase
from selenium import webdriver

class BaseTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('http://www.python.org/')

    def tearDown(self):
        self.driver.refresh()
        self.driver.quit()



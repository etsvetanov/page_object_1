from unittest import TestCase
from selenium import webdriver


class BaseTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.python.org/')

    def tearDown(self):
        self.driver.refresh()
        self.driver.quit()



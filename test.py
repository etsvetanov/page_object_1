from unittest import TestCase
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# caps = DesiredCapabilities.FIREFOX
#
# caps['marionette'] = True
# caps['binary'] = '/Applications/Firefox.app/Contents/MacOS/firefox-bin'

class BaseTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome('~/Documents/WebDriver/chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://www.python.org/')

    def tearDown(self):
        self.driver.refresh()
        self.driver.quit()



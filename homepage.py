from base import BasePage
from base import InvalidPageException

class HomePage(BasePage):
    _home_page_slideshow_locator = 'div.introduction p'

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")

from base import BasePage
from base import InvalidPageException
from locators import article_selectors

class ArticlePage(BasePage):
    _article_locator = '.article-header'

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def title(self):
        return self.driver.find_element_by_css_selector(article_selectors['article_title_locator']).text.strip()

    @property
    def number(self):
        return self.driver.find_element_by_css_selector(article_selectors['article_number_locator']).text.strip()


    @property
    def status(self):
        return self.driver.find_element_by_css_selector(article_selectors['article_status_locator']).text.strip()

    @property
    def author(self):
        return self.driver.find_element_by_css_selectorar(article_selectors['article_author_locator']).text.strip()

    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self._article_locator)
        except:
            raise InvalidPageException('Article page not loaded')


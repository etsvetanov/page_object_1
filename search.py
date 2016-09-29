from base import BasePage
from base import InvalidPageException
from article import ArticlePage

class SearchRegion(BasePage):
    _search_box_locator = 'q'

    def __init__(self, driver):
        super().__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver.find_element_by_name(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()

        return SearchResults(self.driver)


class SearchResults(BasePage):
    _results_page_locator   = 'section.main-content h2'
    _result_list_locator    = 'ul.list-recent-events.menu li'
    _article_name_locator   = 'h3 a'
    _article_link           = 'h3 a'
    _page_title_locator     = 'title'

    _articles_count = 0
    _articles = {}

    def __init__(self, driver):
        super().__init__(driver)

        results = self.driver.find_elements_by_css_selector(self._result_list_locator)

        for result in results:
            name = result.find_element_by_css_selector(self._article_name_locator).text
            self._articles[name] = result.find_element_by_css_selector(self._article_link)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self._results_page_locator)
        except:
            raise InvalidPageException('Search results not loaded')

    @property
    def article_count(self):
        return len(self._articles)

    def get_articles(self):
        return self._articles

    def open_article_page(self, article_name):
        self._articles[article_name].click()
        return ArticlePage(self.driver)



import unittest
from homepage import HomePage
from test import BaseTestCase


class SearchArticleTest(BaseTestCase):
    def test_search_for_article(self):
        homepage = HomePage(self.driver)

        search_results = homepage.search.searchFor('decorators')
        self.assertEqual(20, search_results.article_count)
        article = search_results.open_article_page('PEP 3129 -- Class Decorators')
        self.assertEqual('Class Decorators', article.title)
        self.assertEqual('3129', article.number)
        self.assertEqual('Final', article.status)


if __name__ == '__main__':
    unittest.main(verbosity=5)
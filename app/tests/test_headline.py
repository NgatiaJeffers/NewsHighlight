import unittest
from app.models import Headlines

class HeadlinesTest(unittest.TestCase):
    '''
    Test class to test the behavior of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headline = Headlines('bbc news', 'Hello world!', 'A news to test our source', 'https://www.google.io/img/Mountain', 'https://www.google.io/img/Mountain',  'Google')

    def tearDown(self):
        self.new_source = None

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline, Headlines))

    def test_init_author(self):
        self.assertEqual(self.new_headline.author, 'bbc news')

    def test_init_url(self):
        self.assertEqual(self.new_headline.url, 'https://www.google.io/img/Mountain')

    def test_init_urlToImage(self):
        self.assertEqual(self.new_headline.name, 'https://www.google.io/img/Mountain')

    def test_init_counrty(self):
        self.assertEqual(self.new_headline.country, 'UK')

    def test_init_description(self):
        self.assertEqual(self.new_headline.description, 'A news to test our source')

    def test_init_published(self):
        self.assertEqual(self.new_headline.published, 'Google')
if __name__ == '__main__':
    unittest.main()
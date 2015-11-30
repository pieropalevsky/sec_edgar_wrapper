from sec_edgar_wrapper.utils import full_filing_url
from unittest import TestCase


class UtilsTestCase(TestCase):

    def test_full_filling_url(self):
        actual = full_filing_url('www.test.com/test-index.htm')
        expected = 'www.test.com/test.txt'
        self.assertEqual(actual, expected)
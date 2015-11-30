from unittest import TestCase
import json

from sec_edgar_wrapper.wrapper import SECEdgarWrapper


class SECEdgarWrapperTestCase(TestCase):

    def setUp(self):
        self.wrapper_1 = SECEdgarWrapper(cik='0001397144',
                                         filing_type='13F',
                                         pagination=40,
                                         date_before='20151129',
                                         ownership='exclude')

    def test_query_string(self):
        self.assertIn('count=40', self.wrapper_1._query_string)
        self.assertIn('owner=exclude', self.wrapper_1._query_string)
        self.assertIn('CIK=0001397144', self.wrapper_1._query_string)
        self.assertIn('dateb=20151129', self.wrapper_1._query_string)
        self.assertIn('type=13F', self.wrapper_1._query_string)

    def test_next_page(self):
        test_dict = self.wrapper_1.next_page()
        with open('tests/mocks/wrapper_entry_mock.txt', 'r') as f:
            entry = f.read()
        self.assertEqual(entry, json.dumps(test_dict['entry'][0], indent=2))

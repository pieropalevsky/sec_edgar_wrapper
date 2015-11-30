from sec_edgar_wrapper.parsers import Form13FHR, BaseParser
from unittest import TestCase


class BaseParserTestCase(TestCase):

    def setUp(self):
        with open('tests/mocks/13FHR_mock.txt', 'r') as f:
            text = f.read()
            self.base_parser_1 = BaseParser(text)
            self.base_parser_1_text = text

    def test_text_attribute(self):
        self.assertEqual(self.base_parser_1_text, self.base_parser_1.text)


class Form13FHRTextCase(TestCase):
    def setUp(self):
        with open('tests/mocks/13FHR_mock.txt', 'r') as f:
            text = f.read()
            self.Form13_1 = Form13FHR(text)

        with open('tests/mocks/13FHR_info_table_mock.txt', 'r') as f:
            info_table = f.read()
            self.Form13_1_info_table = info_table

    def test_info_table_property(self):
        self.assertEqual(self.Form13_1.info_table, self.Form13_1_info_table)
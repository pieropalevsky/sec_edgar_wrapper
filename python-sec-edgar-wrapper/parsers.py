from bs4 import BeautifulSoup


class BaseParser:
    """
    Attributes:
        text (str): full str of filing
    """
    def __init__(self, text):
        self.text = text


class Form13FHR(BaseParser):

    @property
    def info_table(self):
        """
        Returns:
             13F-HR information table containing companies owned
        """
        soup = BeautifulSoup(self.text, 'xml')
        information_table = soup.find('informationTable')
        return str(information_table)

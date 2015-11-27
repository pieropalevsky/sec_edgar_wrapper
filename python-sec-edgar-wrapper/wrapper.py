import urllib.parse
import itertools

import xmltodict
import requests

from utils import full_filing_url


class SECEdgarWrapper:
    """Wrapper for the SEC EDGAR site and RSS feeds that mimics an API

    Class Attributes:
        base_company_url (str): base SEC EDGAR RSS url

    Attributes:
        _page_iterator: A private iterator that keeps track of pagination
        cik (str): A string of the cik of the company being searched
        query_string (str): The query string constructed from the arguments
    """

    base_company_url = 'https://www.sec.gov/cgi-bin/browse-edgar' \
                       '?action=getcompany&output=atom&'

    def __init__(self, cik, filing_type='', pagination=40,
                 date_before='',  # (YYYYMMDD)
                 ownership='exclude'  # exclude, include, or only
                 ):
        """
        Arguments:
            cik (str): A string of the cik of the company being searched
            filing_type (str): A string of the filing type being searched
            pagination (int): Max results per page
            date_before (str): A date string in YYYYMMDD format
            ownership (str): Whether to exclude, include or filter for only
                ownership forms
        """

        self._page_iterator = itertools.count(start=0, step=pagination)
        self.cik = cik
        self.query_string = urllib.parse.urlencode({'CIK': cik,
                                                    'type': filing_type,
                                                    'count': pagination,
                                                    'dateb': date_before,
                                                    'owner': ownership,
                                                    })

    def next_page(self):
        """

        Returns:
            An ordered dict with the search company info as well as the search
             results under the key 'entry'
        """
        page_query = '&' + urllib.parse.urlencode(
            {'start': next(self._page_iterator)})
        feed_url = self.base_company_url + self.query_string + page_query
        feed = requests.get(feed_url).text
        feed_dict = xmltodict.parse(feed)

        # the following overwrites the index link with the full filing text
        for entry in feed_dict['feed']['entry']:
            entry['content']['filing-href'] = full_filing_url(entry['content']['filing-href'])
            entry['link']['@href'] = full_filing_url(entry['link']['@href'])
        return feed_dict['feed']

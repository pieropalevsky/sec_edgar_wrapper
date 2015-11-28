def full_filing_url(index_url):
    """
    Arguments:
        A url pointing at the human readable SEC EDGAR Filing index

    Returns:
        A url pointing at the full form
    """
    return index_url.replace('-index.htm', '.txt')

# sec_edgar_wrapper

sec_edgar_wrapper is a work in progress wrapper for SEC Edgar API or lack thereof. It also contains parsers the following forms

  - 13F-HR
  - More will be added as needed

# Installation

    $ pip install sec_edgar_wrapper

# Usage

  - If there are 0 results len(page['entry']) will be 0 instead of a 404 response
  - Beware of amendments to forms they will still show up
  - For some reason accession-number is misspelled as "accession-nunber", I could fix this but I'm leaving it for now

# TODO
- Tests

# Example

    import json
    
    from sec_edgar_wrapper import SECEdgarWrapper
    
    
    api_call = SECEdgarWrapper(cik='0001263508', filing_type="13F")
    page = api_call.next_page()
    print(json.dumps(page, indent=2))

    {
      "@xmlns": "http://www.w3.org/2005/Atom",
      "author": {
        "email": "webmaster@sec.gov",
        "name": "Webmaster"
      },
      "company-info": {
        "addresses": {
          "address": [
            {
              "@type": "mailing",
              "city": "NEW YORK",
              "state": "NY",
              "street1": "667 MADISON AVE",
              "street2": "667 MADISON AVE",
              "zip": "10065"
            },
            {
              "@type": "business",
              "city": "NEW YORK",
              "phone": "2123395600",
              "state": "NY",
              "street1": "667 MADISON AVE",
              "street2": "667 MADISON AVE",
              "zip": "10065"
            }
          ]
        },
        "cik": "0001263508",
        "cik-href": "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001263508&owner=exclude&count=40",
        "conformed-name": "BAKER BROS. ADVISORS LP",
        "fiscal-year-end": "1231",
        "formerly-names": {
          "@count": "1",
          "names": {
            "date": "2013-07-03",
            "name": "BAKER BROS ADVISORS LLC"
          }
        },
        "state-location": "NY",
        "state-location-href": "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&State=NY&owner=exclude&count=40",
        "state-of-incorporation": "DE"
      },
      "entry": [
        {
          "category": {
            "@label": "form type",
            "@scheme": "http://www.sec.gov/",
            "@term": "13F-HR"
          },
          "content": {
            "@type": "text/xml",
            "accession-nunber": "0001144204-15-065993",
            "act": "34",
            "file-number": "028-10519",
            "file-number-href": "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&filenum=028-10519&owner=exclude&count=40",
            "filing-date": "2015-11-16",
            "filing-href": "http://www.sec.gov/Archives/edgar/data/1263508/000114420415065993/0001144204-15-065993.txt",
            "filing-type": "13F-HR",
            "film-number": "151234425",
            "form-name": "Quarterly report filed by institutional managers, Holdings",
            "size": "65 KB"
          },
          "id": "urn:tag:sec.gov,2008:accession-number=0001144204-15-065993",
          "link": {
            "@href": "http://www.sec.gov/Archives/edgar/data/1263508/000114420415065993/0001144204-15-065993.txt",
            "@rel": "alternate",
            "@type": "text/html"
          },
          "summary": {
            "@type": "html",
            "#text": "<b>Filed:</b> 2015-11-16 <b>AccNo:</b> 0001144204-15-065993 <b>Size:</b> 65 KB"
          },
          "title": "13F-HR  - Quarterly report filed by institutional managers, Holdings",
          "updated": "2015-11-16T16:07:48-05:00"
        },



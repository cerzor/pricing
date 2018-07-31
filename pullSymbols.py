import csv
import urllib
import datetime

def pullFiles():
    dateStamp = datetime.date.today()
    #fileName = symbol + dateStamp.year + dateStamp.month + dateStamp.year

    uri = 'https://www.nasdaq.com/screening/companies-by-name.aspx?exchange=NASDAQ&render=download'
    symbolList = { "NASDAQ": 'https://www.nasdaq.com/screening/companies-by-name.aspx?exchange=NASDAQ&render=download',
            "NYSE": "https://www.nasdaq.com/screening/companies-by-name.aspx?exchange=NYSE&render=download",
            "AMEX": "https://www.nasdaq.com/screening/companies-by-name.aspx?exchange=AMEX&render=download" }
    for key, val in symbolList.iteritems():
        print(key)
        print(val)
        urllib.urlretrieve(val, 'symbols/'+ key +'.CSV')
pullFiles()

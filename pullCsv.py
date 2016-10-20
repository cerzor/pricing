import csv
import urllib
import datetime

def pullCsv(symbol):
    dateStamp = datetime.date.today()
    #fileName = symbol + dateStamp.year + dateStamp.month + dateStamp.year


    uri = 'http://financials.morningstar.com/ajax/exportKR2CSV.html?t=' + symbol
    #response = urllib.urlretrieve(uri)

    urllib.urlretrieve(uri, 'ratios/'+symbol+'.CSV')

#pullCsv("MRO")

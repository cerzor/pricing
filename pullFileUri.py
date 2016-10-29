import csv
import urllib
import datetime

def pullFile(symbol, uri, directory):
    dateStamp = datetime.date.today()
    #fileName = symbol + dateStamp.year + dateStamp.month + dateStamp.year


    #uri = 'http://financials.morningstar.com/ajax/exportKR2CSV.html?t=' + symbol
    #response = urllib.urlretrieve(uri)

    urllib.urlretrieve(uri, directory+symbol+'_'+str(dateStamp)+'.CSV')

symbol='MRO'
pullFile(symbol,'http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=a', 'quotes/')

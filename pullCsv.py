import csv
import urllib
import datetime




dateStamp = datetime.date.today()
#fileName = 'FB' + dateStamp.year + dateStamp.month + dateStamp.year


uri = 'http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB'
#response = urllib.urlretrieve(uri)

urllib.urlretrieve(uri, 'FB.CSV')








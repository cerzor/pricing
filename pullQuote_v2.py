import urllib2
import datetime
import ssl
import json

def newQuote(tkSym):
    dateStamp = datetime.date.today() - datetime.timedelta(days=4)
    if dateStamp.weekday() == 6:
        dateStamp = datetime.date.today() -  datetime.timedelta(days=1)
    elif dateStamp.weekday() == 7:
        dateStamp = datetime.date.today() -  datetime.timedelta(days=2)
    print(dateStamp)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    uri = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + tkSym  + '&apikey=D5O3SQPNUU238ITB'
    resp = urllib2.urlopen(uri)
    data = json.load(resp)["Time Series (Daily)"][str(dateStamp)]['4. close']
#    data = urllib.request.urlopen(uri, context=ctx).read() 
#    jsonData = json.loads(data)["Time Series (Daily)"]['2018-05-25']['4. close']
 #   print(jsonData)
    loadQuery = []
    loadQuery.append("INSERT INTO TICKER_PRICE VALUES (\'" + tkSym + "\',\'" + data + "\',\'" + str(dateStamp) + "\')")
    return loadQuery



import urllib.request
import datetime
import ssl
import json

def newQuote():
    dateStamp = datetime.date.today()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    uri = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=D5O3SQPNUU238ITB'
    data = urllib.request.urlopen(uri, context=ctx).read() 
    jsonData = json.loads(data)["Time Series (Daily)"]['2017-12-13']['4. close']
    print(jsonData)

newQuote()

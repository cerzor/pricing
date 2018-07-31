import urllib2
import datetime
import ssl
import json

def newQuote(tkSym, retries):
    dateStamp = datetime.date.today() - datetime.timedelta(days = 1)
    if dateStamp.weekday() == 5:
        dateStamp = datetime.date.today() -  datetime.timedelta(days=2)
    elif dateStamp.weekday() == 6:
        dateStamp = datetime.date.today() -  datetime.timedelta(days=3)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

#CQ7O8SU9QVU5MNIH
    if retries > 10: return 'FAIL'
    try:
      uri = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + tkSym  + '&apikey=CQ7O8SU9QVU5MNIH'
      resp = urllib2.urlopen(uri)
      data = json.load(resp)["Time Series (Daily)"][str(dateStamp)]['4. close']
      print(data)
      loadQuery = []
      loadQuery.append("INSERT INTO TICKER_PRICE VALUES (\'" + tkSym + "\',\'" + data + "\',\'" + str(dateStamp) + "\')")
      return loadQuery
    except:
        retries+=1
        newQuote(tkSym, retries)
        pass
    #        return 'FAIL'
    #        pass


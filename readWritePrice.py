import csv
import datetime

def readWritePrice(symbol):
    dateStamp = str(datetime.date.today())
    file = open('quotes/' + symbol + '_' + str(dateStamp) + '.CSV')
    csv_f = csv.reader(file, skipinitialspace=True)
    infoList = []
    for row in csv_f:
                   infoList.append(row)
    file.close()
##    print infoLis
    price = str(infoList[0])[2:-2]
    loadQuery = []
    loadQuery.append("INSERT INTO PRICINGAPP.TICKER_PRICE(SYMBOL,PRICE,DATE) VALUES ( '" + symbol + "','" + price + "','" + dateStamp + "')")
    print loadQuery[0]
    return loadQuery

#readWritePrice("MRO")

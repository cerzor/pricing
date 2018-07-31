import connectDb
import pullCsv
import loadCsv
import os
import writeData
import pullQuote_v2 as pq
from time import sleep
import timeit
import loadSymbols as ls 

pw = ""
startTime = timeit.default_timer()
symbols = ls.generateSymbolSql()
print("truncating TICKER")
truncateStatement = ['truncate table TICKER']
writeData.writeData(truncateStatement, pw)
print("Loading Ticker Data")
writeData.writeData(symbols, pw)


results = connectDb.pullSymbols(pw)

for result in results:
    print "PROCESSING SYMBOL " + result
    price =  pq.newQuote(result, 0)
    print(price)
    if price != 'FAIL':
        try:
            writeData.writeData(price, pw)
        except:
            print("Error with " + result)
            pass
    pullCsv.pullCsv(result)
  #  print os.stat('ratios/' + result + '.CSV').st_size
    if (os.stat('ratios/' + result + '.CSV').st_size > 100):
        sqlStatements = loadCsv.writeSql(result)
        writeData.writeData(sqlStatements, pw)
    else:
        print "SKIPPING DUE TO FILE SIZE 0 " + result
    sleep(5)
stopTime = timeit.default_timer()

print "RUN TIME: " + str(stopTime - startTime)

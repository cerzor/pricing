import connectDb
import pullCsv
import loadCsv
import os
import writeData
import pullQuote_v2 as pq
from time import sleep
import timeit

startTime = timeit.default_timer()
results = connectDb.pullSymbols()
#print results

for result in results:
    print "PROCESSING SYMBOL " + result
    price =  pq(result)
    pullCsv.pullCsv(result)
  #  print os.stat('ratios/' + result + '.CSV').st_size
    if (os.stat('ratios/' + result + '.CSV').st_size > 100):
        sqlStatements = loadCsv.writeSql(result)
        writeData.writeData(sqlStatements)
    else:
        print "SKIPPING DUE TO FILE SIZE 0 " + result
#    sleep(3)
stopTime = timeit.default_timer()

print "RUN TIME: " + str(stopTime - startTime)

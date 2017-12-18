from readWritePrice import readWritePrice
import connectDb
from time import sleep
import timeit
import os
import datetime
import pullFileUri
import writeData

dateStamp = str(datetime.date.today())
startTime = timeit.default_timer()
results = connectDb.pullSymbols()

for result in results:
    print "PROCESSING SYMBOL " + result
    fileLocation = 'quotes/' + result + '_' + dateStamp + '.CSV'
    pullFileUri.pullFile(result, 'http://download.finance.yahoo.com/d/quotes.csv?s='+result+'&f=a', 'quotes/')
    if(os.stat(fileLocation) > 0):
        sqlStatements = readWritePrice(result)
        writeData.writeData(sqlStatements)
    else:
        print "SKIPPING DUE TO 0 FILE SIZE " + result


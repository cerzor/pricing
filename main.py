import connectDb
import pullCsv
import loadCsv
import os
import writeData

results = connectDb.pullSymbols()
#print results

for result in results:
    print "PROCESSING SYMBOL " + result
    pullCsv.pullCsv(result)
  #  print os.stat('ratios/' + result + '.CSV').st_size
    if (os.stat('ratios/' + result + '.CSV').st_size > 0):
        sqlStatements = loadCsv.writeSql(result)
        writeData.writeData(sqlStatements)
    else:
        print "SKIPPING DUE TO FILE SIZE 0 " + result

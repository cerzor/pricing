import csv

def generateSymbolSql():
    exchangeArr = ['NASDAQ','AMEX','NYSE']
    for ex in exchangeArr:
        file = open('symbols/' + ex + '.CSV')
        csv_f = csv.reader(file, skipinitialspace=True)

        infoList = []
        for row in csv_f:
        	    if row and csv_f.line_num > 1:
                       infoList.append(row)
                    elif not row:
                	break
        file.close()
        loadQuery = []
        test = " ";
        for count, column in enumerate(infoList):
          #loadQuery.append("""insert into TICKER  VALUES ('"")
          test = "insert into TICKER  VALUES ("
          for i,c in enumerate(column):
              if(str(c) != "" and  i != 2 and i!=7):
                test = test + "\'"  + str(c).replace("$", "").replace(",","") + "\',"
          test = test[:-1] + ",\'" + ex + "\',\'I\')"
          loadQuery.append(test)

    return loadQuery

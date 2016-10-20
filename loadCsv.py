import csv

def writeSql(tickerSymbol):
    file = open('ratios/' + tickerSymbol + '.CSV')
    csv_f = csv.reader(file, skipinitialspace=True)

    infoList = []
    for row in csv_f:
    	    if row and csv_f.line_num > 2:
                   infoList.append(row)
            elif not row:
	        	break
    file.close()


    loadQuery = []
    for column in infoList[0]:
        if (column != "TTM" and column != ""): 
    #        print column
            loadQuery.append("""insert into SYM_KR_FINANCE ( 
            SYMBOL
            ,`YEAR`
            ,REVENUE
            ,GROSS_MARGIN
            ,OPERATE_INCOM
            ,OPERATING_MARGIN
            ,NET_INCOME
            ,EPS
            ,DIVIDENDS
            ,PAYOUT_RATIO
            ,SHARES
            ,BOOK_VALUE_PS
            ,OPERATING_CF
            ,CAP_SPENDING
            ,FCF
            ,FCF_PS
            ,WORKING_CAPITAL
            ) VALUES ('""" + tickerSymbol +"','" + column + "','")

    loopIndex = 1
    while loopIndex < 16:
        for index, rev in enumerate(infoList[loopIndex]):
             ## print str(rev) + " " + str(index)
            if(index !=  0  and index < 11):
               # print rev
                curIndex = index - 1
                if(loopIndex != 15):
                    loadQuery[curIndex] = loadQuery[curIndex] + rev +"','"
                else:
                    loadQuery[curIndex] = loadQuery[curIndex] + rev +"')"
        loopIndex += 1

    #for item in loadQuery:    
    #     print item
    return loadQuery
#writeSql("","")

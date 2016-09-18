import csv

file = open('/home/pi/git/pricing/FB.CSV')
csv_f = csv.reader(file)
for row in csv_f:
	if row and csv_f.line_num > 2:
                print row
        elif not row:
		break

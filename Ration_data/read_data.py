
import csv
fields=[]
rows=[]
i=0
with open('jss.csv','r') as csv_input:
	csvreader= csv.reader(csv_input)
	fields=next(csvreader)
	for row in csvreader:
		rows.append(row)
k=0
data=[]
for row in rows:
    if k%2!=0:
        data.append(row)
    k+=1        

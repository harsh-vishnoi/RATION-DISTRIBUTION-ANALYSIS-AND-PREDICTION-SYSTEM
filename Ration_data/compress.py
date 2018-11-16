
import csv
import random
fields=[]
rows=[]
i=0
with open('Test_Data.csv','r') as csv_input:
	csvreader= csv.reader(csv_input)
	fields=next(csvreader)
	for row in csvreader:
		rows.append(row)
data = []      
family = []
new=[]
fields.append('male')
fields.append('female')
i=0
while(i<=4099):
    count=int(rows[i][9])
    j=0
    while(j<count):
        family.append(rows[j+i])
        j+=1
    i=i+count-1
    data.append(family[0][0])        
    data.append(family[0][1])        
    data.append(family[0][2])        
    data.append(family[0][3])
    sum1=0
    m=0
    f=0
    cal=0
    sal=0
    for r in family:  
        sum1=sum1+int(r[4])
        if r[5]=="Male":
            m+=1
        elif r[5]=="Female":
            f+=1
        cal=cal+int(r[8])   
        sal=sal+float(r[11])
    data.append(sum1/len(family))
    data.append(family[0][5])        
    data.append(family[0][6])        
    data.append(family[0][7])        
    data.append(cal)        
    data.append(family[0][9])        
    data.append(family[0][10])        
    data.append(sal)
    data.append(m)
    data.append(f)
    i+=1      
    new.append(data)
    family=[]
    data=[]
with open('jss.csv','w') as csvfile:
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(new)    
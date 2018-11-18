import math
govt_cal=7500000
import csv
fields=[]
rows=[]
i=0
with open('File_with_clusters_5.csv','r') as csv_input:
	csvreader= csv.reader(csv_input)
	fields=next(csvreader)
	for row in csvreader:
		rows.append(row)
cal=[0,0,0,0,0,0,0,0]    
for row in rows:
    if int(row[20])==0:
        cal[0]=cal[0]+float(row[19])
    if int(row[20])==1:
        cal[1]=cal[1]+float(row[19])
    if int(row[20])==2:
        cal[2]=cal[2]+float(row[19])
    if int(row[20])==3:
        cal[3]=cal[3]+float(row[19])
    if int(row[20])==4:
        cal[4]=cal[4]+float(row[19])
    if int(row[20])==5:
        cal[5]=cal[5]+float(row[19])
    if int(row[20])==6:
        cal[6]=cal[6]+float(row[19])
    if int(row[20])==7:
        cal[7]=cal[7]+float(row[19])
      
total_cal=sum(cal)

decrement=govt_cal/total_cal
if decrement<=1:
    for i in range(8):
        cal[i]=cal[i]*decrement 
cal_original=cal[:] 

if decrement>.9 and decrement<1:  
    a1=cal[3]*.1
    cal[1]+=a1
    cal[3]-=a1
    a2=cal[4]*.08
    cal[4]-=a2
    cal[5]+=a2
    a3=cal[0]*.05
    cal[0]-=a3
    cal[6]+=a3
    a4=cal[2]*.03
    cal[7]+=a4
    cal[2]-=a4
elif decrement>.7 and decrement<=.9:
    a1=cal[3]*.2
    cal[1]+=a1
    cal[3]-=a1
    a2=cal[4]*.15
    cal[4]-=a2
    cal[5]+=a2
    a3=cal[0]*.1
    cal[0]-=a3
    cal[6]+=a3
    a4=cal[2]*.05
    cal[7]+=a4
    cal[2]-=a4 
    
elif decrement<=.7:
    a1=cal[3]*.3
    cal[1]+=a1
    cal[3]-=a1
    a2=cal[4]*.20
    cal[4]-=a2
    cal[5]+=a2
    a3=cal[0]*.15
    cal[0]-=a3
    cal[6]+=a3
    a4=cal[2]*.1
    cal[7]+=a4
    cal[2]-=a4
       

calculated_cal=[]
k1=(cal[1]/cal_original[1])
k2=(cal[5]/cal_original[5])
k3=(cal[6]/cal_original[6])
k4=(cal[7]/cal_original[7])
m=0
k=0
min1=99999999
for row in rows:
    m+=1
    if int(row[20])==0:
        cal[0]=cal[0]-float(row[19])*decrement*.85
        calculated_cal.append(float(row[19])*decrement*.85)
        
        if min1>(float(row[19])*decrement*.85):
            min1=(float(row[19])*decrement*.85)
            k=m
    if (int(row[20])==1):
        cal[1]=cal[1]-float(row[19])*decrement*k1
        calculated_cal.append(float(row[19])*decrement*k1)
        
        if min1>float(row[19])*decrement*k1:
            min1=float(row[19])*decrement*k1
            k=m
    if int(row[20])==2:
        cal[2]=cal[2]-float(row[19])*decrement*.9
        calculated_cal.append(float(row[19])*decrement*.9)
        
        if min1>float(row[19])*decrement*.9:
            min1=float(row[19])*decrement*.9
            k=m
    if int(row[20])==3:
        cal[3]=cal[3]-float(row[19])*decrement*.6
        calculated_cal.append(float(row[19])*decrement*.6)
        
        if min1>float(row[19])*decrement*.6:
            min1=float(row[19])*decrement*.6
            k=m
    if int(row[20])==4:
        cal[4]=cal[4]-float(row[19])*decrement*.75
        calculated_cal.append(float(row[19])*decrement*.75)
        
        if min1>float(row[19])*decrement*.75:
            min1=float(row[19])*decrement*.75
            k=m
    if int(row[20])==5:
        cal[5]=cal[5]-float(row[19])*decrement*k2
        calculated_cal.append(float(row[19])*decrement*k2)
        if min1>float(row[19])*decrement*k2:
            min1=float(row[19])*decrement*k2
            k=m
            
    if int(row[20])==6:
        cal[6]=cal[6]-float(row[19])*decrement*k3
        calculated_cal.append(float(row[19])*decrement*k3)
        
        if min1>float(row[19])*decrement*k3:
            min1=float(row[19])*decrement*k3
            k=m
    if int(row[20])==7:
        cal[7]=cal[7]-float(row[19])*decrement*k4
        calculated_cal.append(float(row[19])*decrement*k4)
        
        if min1>float(row[19])*decrement*k4:
            min1=float(row[19])*decrement*k4
            k=m
for i in range(8):
    cal[i]=round(cal[i])

print(calculated_cal)

#Adding to the main dataset
import csv
rows=[]
fields=[]
with open('File_with_clusters_5.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("Salary Final")
i=0        
for row in rows:
    row.append(calculated_cal[i])
    i+=1        

with open('Final_data_file_6.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    


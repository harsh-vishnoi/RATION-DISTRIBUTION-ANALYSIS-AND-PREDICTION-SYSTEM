import csv
import random
fields=[]
rows=[]
i=0
with open('hh.csv','r') as csv_input:
	csvreader= csv.reader(csv_input)
	fields=csvreader.next()
	for row in csvreader:
		rows.append(row)

age = 0
gender = ""
sex = 0
ctr = 0
leave = 0
fields.append("Calories")	

for row in rows:
    if row[4] == "ids_familyrelation_age" or row[4] == "":
        continue
    #print (row[1])  # Only print the column in the row
    i_age = int(row[4])
    age = (i_age)
    gender = row[5]
    if gender == "Female":
        sex = 0
    else:
        sex = 1
        

    if sex == 0:
        if age<2:
            calories = random.randint(510,850)
        elif age>=2 and age<=3:
            calories = random.randint(1000,1400)
        elif age>=4 and age<=8:
            calories = random.randint(1400,1600)
        elif age>=9 and age<=13:
            calories = random.randint(1600,2000)
        elif age>=14 and age<=18:
            calories = random.randint(2000,2100)
        elif age>=19 and age<=30:
            calories = random.randint(2000,2200)
        elif age>=31 and age<=50:
            calories = random.randint(1950,2100)
        else:
            calories = random.randint(1750,1850)
    elif sex == 1:
        if age<2:
            calories = random.randint(510,850)
        elif age>=2 and age<=3:
            calories = random.randint(1000,1400)
        elif age>=4 and age<=8:
            calories = random.randint(1400,1600)
        elif age>=9 and age<=13:
            calories = random.randint(1800,2200)
        elif age>=14 and age<=18:
            calories = random.randint(2400,2800)
        elif age>=19 and age<=30:
            calories = random.randint(2600,2800)
        elif age>=31 and age<=50:
            calories = random.randint(2400,2600)
        else:
            calories = random.randint(2200,2400)

    row.append(calories)

fields.append('Count')
for r in rows:
	name=r[1]
	c=0
	for r2 in rows:
		if r[1]==r2[1]:
			c+=1
	r.append(c)	
fields.append('job')
k=0
for r in rows:
	#convert r[4] to integer
	r1=int(r[4])
	if(r1>17 and r1<52) and r[5]=="Male":
		k=random.choice([0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1])
		r.append(k)
		print(k)
	elif r1<=17 or r1>=52:
		r.append(0)
	elif(r1>17 and r1<25):
		
		k=random.choice([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0])
		r.append(k)
	elif(r[5]=="Female" and r1<52):
		k=random.choice([0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0])
		r.append(k)	
sal=[100,-100,150,-150,200,-200,0,250,-250,-300,350,-350,300,-400,-400,-450,-500,500,450,0,-550,-600,650,-700,750,-800,900]
fields.append("salary")	


for r in rows:

	if r[10]==1:
		if (int(r[4])>=17 and int(r[4])<=25) or r[5]=="Female":
			val =  random.randint(17,24)*220.00+random.choice(sal)
			r.append(val)
		elif int(r[4])>25 :
			val = random.randint(25,35)*380.00+random.choice(sal*3)		
			r.append(val)
	else:
		r.append("0.00")		




with open('jss.csv','w') as csvfile:
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(rows)

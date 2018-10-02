import csv
import random

"""try:
    risk = open('final data.csv', 'r', encoding="windows-1252").read() #find the file

except:
    while risk != "riskfactors.csv":  # if the file cant be found if there is an error
        print("Could not open", risk, "file")
    risk = input("\nPlease try to open file again: ")
else:
    with open("final data.csv") as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|')

        data = []
        for row in reader:# Number of rows including the death rates 
            for col in (2,4): # The columns I want read   B and D
                data.append(row)
                #data.append(col)"""
fields =[]
row1 = []
with open('final data.csv','r') as f:
            rows = csv.reader(f)
            fields = rows.next() 
            for row in rows:
                row1.append(row)

     
age = 0
gender = ""
sex = 0
ctr = 0
leave = 0

for row in row1:
    if row[4] == "ids_familyrelation_age":
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

with open('data_cal.csv','w') as csvfile:
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(row1)





        
    
    

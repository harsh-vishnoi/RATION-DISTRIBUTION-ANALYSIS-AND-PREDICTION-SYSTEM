import random
import csv

fields = []
rows= []

with open('Final_data_file_6.csv', 'r') as csv_input:
    csvreader = csv.reader(csv_input)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
rice = []
wheat = []
sugar = []
cal_rice = 0
cal_wheat = 0
cal_sugar = 0
rice = 0
wheat = 0
sugar = 0
cal = 0.0

fields.append("Rice")
fields.append("Wheat")
fields.append("Sugar")

for r in rows:
    cal = float(r[21])
    
    cal_rice = (40/100)*cal
    cal_wheat = (40/100)*cal
    cal_sugar = (20/100)*cal
    rice = cal_rice*(1/4)
    wheat = cal_wheat*(1/4)
    sugar = cal_sugar*(1/9)
    r.append(rice)
    r.append(wheat)
    r.append(sugar)
    
with open('Ration.csv','w') as csvfile:
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(rows)


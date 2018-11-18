import csv
fields = []
rows = []
i = 0
with open('compressed_data.csv', 'r') as csv_input:
    csvreader = csv.reader(csv_input)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

k = 0
data = []
for rown in rows:
    if k%2 != 0:
        data.append(rown)
    k = k+1
print(data)

with open('new.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)

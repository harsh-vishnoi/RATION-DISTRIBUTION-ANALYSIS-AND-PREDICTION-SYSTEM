import random
import csv

fields = []
rows= []
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []

C0 = -99
C1 = -99
C2 = -99
C3 = -99
C4 = -99
C5 = -99
C6 = -99
C7 = -99

with open('Final_data_file_6.csv', 'r') as csv_input:
    csvreader = csv.reader(csv_input)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)


for r in rows:
    if int(r[20]) == 0:
        c0.append(r)
    if int(r[20]) == 1:
        c1.append(r)
    if int(r[20]) == 2:
        c2.append(r)
    if int(r[20]) == 3:
        c3.append(r)
    if int(r[20]) == 4:
        c4.append(r)
    if int(r[20]) == 5:
        c5.append(r)
    if int(r[20]) == 6:
        c6.append(r)
    if int(r[20]) == 7:
        c7.append(r)

rnd = 0





headings = ['Names','Count','Male','Female', 'Salary', 'pred_Calories','Final cal', 'Cluster']


C = 98
names = []
count = []
male = []
female = []
sal = []
cal = []
cluster = []
calories = []


while(C != -99):
    C = int(input("Enter cluster : "))

    if C == 0:
        rnd = random.randint(0,len(c0))
        
        names.append(c0[rnd][1])
        count.append(c0[rnd][9])
        male.append(c0[rnd][12])
        female.append(c0[rnd][13])
        sal.append(c0[rnd][11])
        cal.append(c0[rnd][19])
        calories.append(c0[rnd][21])
        cluster.append(c0[rnd][20])
        
    if C == 1:
        rnd = random.randint(0,len(c1))
        
        names.append(c1[rnd][1])
        count.append(c1[rnd][9])
        male.append(c1[rnd][12])
        female.append(c1[rnd][13])
        sal.append(c1[rnd][11])
        cal.append(c1[rnd][19])
        calories.append(c1[rnd][21])
        cluster.append(c1[rnd][20])
    if C == 2:
        rnd = random.randint(0,len(c2))
        
        names.append(c2[rnd][1])
        count.append(c2[rnd][9])
        male.append(c2[rnd][12])
        female.append(c2[rnd][13])
        sal.append(c2[rnd][11])
        cal.append(c2[rnd][19])
        calories.append(c2[rnd][21])
        cluster.append(c2[rnd][20])
    if C == 3:
        rnd = random.randint(0,len(c3))
        
        names.append(c3[rnd][1])
        count.append(c3[rnd][9])
        male.append(c3[rnd][12])
        female.append(c3[rnd][13])
        sal.append(c3[rnd][11])
        cal.append(c3[rnd][19])
        calories.append(c3[rnd][21])
        cluster.append(c3[rnd][20])
    if C == 4:
        rnd = random.randint(0,len(c4))
        
        names.append(c4[rnd][1])
        count.append(c4[rnd][9])
        male.append(c4[rnd][12])
        female.append(c4[rnd][13])
        sal.append(c4[rnd][11])
        cal.append(c4[rnd][19])
        calories.append(c4[rnd][21])
        cluster.append(c4[rnd][20])
    if C == 5:
        rnd = random.randint(0,len(c5))
        
        names.append(c5[rnd][1])
        count.append(c5[rnd][9])
        male.append(c5[rnd][12])
        female.append(c5[rnd][13])
        sal.append(c5[rnd][11])
        cal.append(c5[rnd][19])
        calories.append(c5[rnd][21])
        cluster.append(c5[rnd][20])
    if C == 6:
        rnd = random.randint(0,len(c6))
        
        names.append(c6[rnd][1])
        count.append(c6[rnd][9])
        male.append(c6[rnd][12])
        female.append(c6[rnd][13])
        sal.append(c6[rnd][11])
        cal.append(c6[rnd][19])
        calories.append(c6[rnd][21])
        cluster.append(c6[rnd][20])
    if C == 7:
        rnd = random.randint(0,len(c7))
        
        names.append(c7[rnd][1])
        count.append(c7[rnd][9])
        male.append(c7[rnd][12])
        female.append(c7[rnd][13])
        sal.append(c7[rnd][11])
        cal.append(c7[rnd][19])
        calories.append(c7[rnd][21])
        cluster.append(c7[rnd][20])
    
l0=len("names")
l1=len("count")
l2=len("male")
l3=len("female")
l4=len("salary")
l5=len("predicted calories")
l6=len("final calories")
l7=len("cluster")
for i in names:
    if l0<len(i):
        l0=len(i)
for i in count:
    if l1<len(i):
        l1=len(i)
for i in male:
    if l2<len(i):
        l2=len(i)
for i in female:
    if l3<len(i):
        l3=len(i)
for i in sal:
    if l4<len(i):
        l4=len(i)
for i in cal:
    if l5<len(i):
        l5=len(i)
for i in calories:
    if l6<len(i):
        l6=len(i)
for i in cluster:
    if l7<len(i):
        l7=len(i)


print("| Name "," "*(l0-len('names')), "| Count ", " "*(l1-len('count')), "| Male ", " "*(l2-len('male')), "| Female ", " "*(l3-len('female')), "| Salary " , " "*(l4-len('salary')), "| Predicted calories ", " "*(l5-len('Predicted calories')), "| Final Caloreis ", " "*(l6-len('final calories')), "| Cluster", " "*(l7-len('Cluster')))
for i in range(len(names)):
    print("|", names[i], " "*(l0-len(names[i])), "| ",count[i], " "*(l1-len(count[i])),"| ",male[i], " "*(l2-len(male[i])),"| ",female[i], " "*(l3-len(female[i])),"| ",sal[i], " "*(l4-len(sal[i])),"| ",cal[i], " "*(l5-len(cal[i])),"| ",calories[i], " "*(l6-len(calories[i])),"| ",cluster[i], " "*(l7-len(cluster[i])))

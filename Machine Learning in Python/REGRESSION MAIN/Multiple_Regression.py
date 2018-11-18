import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Final_file_of_family_data.csv')

X = dataset.iloc[:,[4,9,12,13]].values
y = dataset.iloc[:,8].values


#Splitting Data to Training and Test Set

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

#Fitting Multiple Linear Regression To Training Set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting results on Test set
y_pred = regressor.predict(X)


#Predicting a new result 
y_pred = regressor.predict(X)

y_pred = y_pred.ravel()

"""#Adding to the main dataset
import csv
rows=[]
fields=[]
with open('Answer.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("Multiple_Regression_Predicted")
i=0        
for row in rows:
    row.append(y_pred[i])
    i+=1        

with open('Answer.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows) """
    

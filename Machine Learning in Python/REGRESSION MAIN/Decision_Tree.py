# Decision Tree Regression Model 

#Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


 #Importing Dataset

dataset = pd.read_csv('Final_file_of_family_data.csv')
X = dataset.iloc[:,[4,9,12,13]].values
y = dataset.iloc[:,8:9].values




#Splittung the data into training and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=0)


#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Fitting Regressor Model to Dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train,y_train )


#Predicting a new result 
y_pred = regressor.predict(X)

y_pred = y_pred.ravel()

"""#Adding to the main dataset
import csv
rows=[]
fields=[]
with open('compressed_data_clustering.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("Decision_Tree_Predicted")
i=0        
for row in rows:
    row.append(y_pred[i])
    i+=1        

with open('Answer.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    

"""

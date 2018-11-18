#Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the Dataset

dataset = pd.read_csv('Final_file_of_family_data.csv')
X = dataset.iloc[:,[4,9,12,13]].values
y = dataset.iloc[:,8:9].values


#Splittung the data into training and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=0)


#Fitting Multiple Linear Regression To Training Set
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)

#Fitting Polynomial Regression to training and test set
from sklearn.preprocessing import PolynomialFeatures
poly_regressor = PolynomialFeatures(degree = 4)
X_poly = poly_regressor.fit_transform(X_train)
lin_regressor_2 = LinearRegression()
lin_regressor_2.fit(X_poly, y_train)
X_poly_2 = poly_regressor.fit_transform(X)


#Predicting a new result with Linear Regression
linear_regressor.predict(X)

#Predicting a new result with Polynomial Regression
y_pred=lin_regressor_2.predict(X_poly_2)
y_pred = y_pred.ravel()
#Predicting a new result 
#y_pred = regressor_2.predict(X)



"""#Adding to the main dataset
import csv
rows=[]
fields=[]
with open('Answer.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("Polynomial_Predicted")
i=0        
for row in rows:
    row.append(y_pred[i])
    i+=1        

with open('Answer.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)"""
    

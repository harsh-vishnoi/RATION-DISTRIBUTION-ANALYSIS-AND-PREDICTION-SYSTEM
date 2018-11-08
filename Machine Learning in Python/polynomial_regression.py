#Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the Dataset
dataset = pd.read_csv('Test_data.csv')
X = dataset.iloc[:,4:6].values
y = dataset.iloc[:,8:9].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding Dummy Variable Trap

X = X[:,2:]


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


#Visualising the Linear Regression Results
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = X_train[:,0]
y = X_train[:,1]
z = y_train

ax.scatter(x, y, z, c='r', marker='+')

ax.set_title(' Linear Regression ')
ax.set_xlabel(' Male/Female')
ax.set_ylabel(' Age ')
ax.set_zlabel(' Calories ')

x1 = X_test[:,0]
y1 = X_test[:,1]
z1 = linear_regressor.predict(X_test)
ax.scatter(x1, y1, z1, c='b', marker='*')
plt.show()

#Visualising the Polynomial Regression Results
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = X_train[:,0]
y = X_train[:,1]
z = y_train

ax.scatter(x, y, z, c='r', marker='+')

ax.set_title(' Polynomial Regression ')
ax.set_xlabel(' Male/Female')
ax.set_ylabel(' Age ')
ax.set_zlabel(' Calories ')

x1 = X_test[:,0]
y1 = X_test[:,1]
z1 = lin_regressor_2.predict(poly_regressor.fit_transform(X_test))
ax.scatter(x1, y1, z1, c='b', marker='*')
plt.show()

#Predicting a new result with Linear Regression
linear_regressor.predict([1,39])

#Predicting a new result with Polynomial Regression
lin_regressor_2.predict(poly_regressor.fit_transform([1,39]))


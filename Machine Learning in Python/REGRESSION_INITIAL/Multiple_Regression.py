import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Test_Data.csv')

X = dataset.iloc[:,4:6].values
y = dataset.iloc[:,8].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding Dummy Variable Trap

X = X[:,2:]

#Splitting Data to Training and Test Set

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

#Fitting Multiple Linear Regression To Training Set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting results on Test set
y_pred = regressor.predict([1,39])




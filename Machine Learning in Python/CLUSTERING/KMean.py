#Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 #Importing Dataset
 
dataset = pd.read_csv('Test_Data.csv')
X = dataset.iloc[:,[11,9]].values

#Using Elbow method to find the number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++', max_iter = 300, n_init = 10,random_state =0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('No of Clusters')
plt.ylabel('WCSS')
plt.show()

#Applying K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++',max_iter = 300, n_init = 10,random_state = 0)
y_kmeans =  kmeans.fit_predict(X)

#Visualising the Clusters
plt.scatter(X[y_kmeans == 0 , 0], X[y_kmeans == 0 , 1], s = 20, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1 , 0], X[y_kmeans == 1 , 1], s = 20, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2 , 0], X[y_kmeans == 2 , 1], s = 20, c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],s = 100, c = 'yellow', label = 'Centroids')
plt.title('Clusters')
plt.xlabel('Salary of Individual')
plt.ylabel('No of people in family')
plt.legend()
plt.show() 

import csv
import random

fields=[]
rows=[]
i=0
with open('Test_Data.csv','r') as csv_input:
	csvreader= csv.reader(csv_input)
	fields=csvreader.next()
	for row in csvreader:
		rows.append(row)
  
fields.append("Calories_New")


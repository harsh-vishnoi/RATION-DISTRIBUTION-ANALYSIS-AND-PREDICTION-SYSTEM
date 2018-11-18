#Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 #Importing Dataset
 
dataset = pd.read_csv("Final_file_of_family_data_4.csv")
X = dataset.iloc[:,[11,19]].values

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
kmeans = KMeans(n_clusters = 8, init = 'k-means++',max_iter = 300, n_init = 10,random_state = 0)
y_kmeans =  kmeans.fit_predict(X)

#Visualising the Clusters
plt.scatter(X[y_kmeans == 0 , 0],X[y_kmeans == 0 , 1], s = 20, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1 , 0],X[y_kmeans == 1 , 1], s = 20, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2 , 0],X[y_kmeans == 2 , 1], s = 20, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3 , 0],X[y_kmeans == 3 , 1], s = 20, c = 'brown', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4 , 0],X[y_kmeans == 4 , 1], s = 20, c = 'black', label = 'Cluster 5')
plt.scatter(X[y_kmeans == 5 , 0],X[y_kmeans == 5 , 1], s = 20, c = 'orange', label = 'Cluster 6')
plt.scatter(X[y_kmeans == 6 , 0],X[y_kmeans == 6 , 1], s = 20, c = 'pink', label = 'Cluster 7')
plt.scatter(X[y_kmeans == 7 , 0],X[y_kmeans == 7 , 1], s = 20, c = 'purple', label = 'Cluster 8')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],s = 100, c = 'yellow', label = 'Centroids')
plt.title('Clusters')
plt.xlabel('Salary')
plt.ylabel('Calories')
plt.legend()
plt.show() 

#Adding to the main dataset

import csv
rows=[]
fields=[]
with open('Desktop/PROJECTS/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/Ration_data/"File_with_clusters_5.csv"','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("CLUSTERS")
i=0        
for row in rows:
    row.append(y_kmeans[i])
    i+=1        

with open('Desktop/PROJECTS/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/Ration_data/"File_with_clusters_5.csv"','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    


#Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 #Importing Dataset
 
dataset = pd.read_csv('Desktop/PROJECTS/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/Machine Learning in Python/CLUSTERING/compressed_data.csv')
X = dataset.iloc[:,[4,9,11,12,13]].values

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
kmeans = KMeans(n_clusters = 5, init = 'k-means++',max_iter = 300, n_init = 10,random_state = 0)
y_kmeans =  kmeans.fit_predict(X)



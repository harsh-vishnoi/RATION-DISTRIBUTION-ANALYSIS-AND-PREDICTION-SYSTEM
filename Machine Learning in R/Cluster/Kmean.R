# K Mean Clustering
dataset <- read.csv('RF_Final.csv')
X <- dataset[13:14]


#Elbow method
set.seed(6)
wcss <- vector()
for(i in 1:10) wcss[i] <- sum(kmeans(X, i)$withinss)
plot(1:10, wcss, type = 'b', main = paste('clusters of clients'), xlab = 'No of clusters', ylab = 'wcss')

# Applying K means to the dataset
options(max.print=999999)
set.seed(29)
kmeans <- kmeans(X, 8, iter.max = 300, nstart = 10)

# Plotting graph
#install.packages('cluster')
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('CLUSTER'),
         xlab = 'salary',
         ylab = 'no of people in family')
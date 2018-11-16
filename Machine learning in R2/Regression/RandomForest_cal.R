#Random Forest

#importing the dataset
dataset = read.csv('compressed_data.csv')
dataset = dataset[8:12]



#splitting the data
set.seed(123)
split = sample.split(dataset$Calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#install.packages('randomForest')
#Fitting
library(randomForest)
regressor = randomForest(x = training_set[2:5],
                         y = training_set$Calories,
                         ntree = 100)
#predicting
pred_RF = predict(regressor, newdata = dataset)

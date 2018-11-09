#Random Forest

#importing the dataset
dataset = read.csv('Test1_new.csv')

#categorical data
dataset$ids_familyrelation_gender = factor(dataset$ids_familyrelation_gender,
                                           levels = c('Female', 'Male'),
                                           labels = c(0,1))

dataset = dataset[, 5:7]



#splitting the data
set.seed(123)
split = sample.split(dataset$calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#install.packages('randomForest')
#Fitting
regressor = randomForest(x = training_set[, 1:2],
                         y = training_set$calories,
                         ntree = 100)
#predicting
y_pred = predict(regressor, newdata = test_set)
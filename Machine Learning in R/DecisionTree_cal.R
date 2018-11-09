#Decision Tree

#Impoerting the Dataset
dataset = read.csv('Test1_new.csv')

#categorical data
dataset$ids_familyrelation_gender = factor(dataset$ids_familyrelation_gender,
                                           levels = c('Female', 'Male'),
                                           labels = c(0,1))

dataset = dataset[, 5:7]

set.seed(123)

#splitting the dataset
split = sample.split(dataset$calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#install.packages('rpart')
#Fitting the Decision tree to the dataset
regressor = rpart(formula = dataset$calories ~ dataset$ids_familyrelation_gender + dataset$ids_familyrelation_age,
                  data = training_set,
                  control = rpart.control(minsplit = 2))
#predicting
y_pred = predict(regressor, newdata = test_set)
#Decision Tree

#Impoerting the Dataset
dataset = read.csv('compressed_data.csv')
dataset = dataset[7:12]



set.seed(123)

#splitting the dataset
split = sample.split(dataset$Calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#install.packages('rpart')
#Fitting the Decision tree to the dataset
library(rpart)
regressor = rpart(formula = Calories ~ salary + Count + male + female + selection4_familyrelation_age,
                  data = training_set,
                  control = rpart.control(minsplit = 2))
#predicting
pred_DT = predict(regressor, newdata = dataset)
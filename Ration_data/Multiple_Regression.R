dataset = read.csv('Test_Data.csv')

# Encoding categorical data
dataset$selection4_familyrelation_gender = factor(dataset$selection4_familyrelation_gender,
                                                  levels = c('Female', 'Male'),
                                                  labels = c(1, 2))

library(caTools)
set.seed(123)
split=sample.split(dataset$Calories, SplitRatio = 0.6)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

#Fitting Multiple Linear Regression to Training Set
regressor = lm( formula = Calories ~ selection4_familyrelation_gender + selection4_familyrelation_age,
                data = training_set)

#Predicting The test set result

y_pred = predict(regressor, newdata= test)

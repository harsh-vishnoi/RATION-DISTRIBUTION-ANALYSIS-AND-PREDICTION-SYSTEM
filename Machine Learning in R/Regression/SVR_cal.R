# SVR

# Importing the dataset
dataset = read.csv('compressed_data.csv')
dataset = dataset[7:12]


#splitting
set.seed(123)
split = sample.split(dataset$Calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#fitting the model
#install.packages('e1071')
library(e1071)
regressor = svm(formula = Calories ~ salary + Count + male + female + selection4_familyrelation_age,
                data = training_set,
                type = 'eps-regression')

#predict
pred_SVR = predict(regressor, newdata = dataset)
# SVR

# Importing the dataset
dataset = read.csv('Test1.csv')

#categorical data
dataset$ids_familyrelation_gender = factor(dataset$ids_familyrelation_gender,
                                           levels = c('Female', 'Male'),
                                           labels = c(0,1))

#splitting
set.seed(123)
split = sample.split(dataset$calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#fitting the model
#install.packages('e1071')
regressor = svm(formula = calories ~ ids_familyrelation_age + ids_familyrelation_gender,
                data = training_set,
                type = 'eps-regression')

#predict
y_pred = predict(regressor, newdata = test_set)
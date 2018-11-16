# Multiple Linear regression
 
# Importing the dataset
dataset = read.csv('Test1.csv')

# Encoding the categorical data
dataset$ids_familyrelation_gender = factor(dataset$ids_familyrelation_gender,
                                           levels = c('Female', 'Male'),
                                           labels = c(0,1))

set.seed(123)

# Splitting the dataset into test set and training set
split = sample.split(dataset$calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting the Multiple Linear Regression model to the training set
regressor = lm(formula = calories ~ ids_familyrelation_gender + ids_familyrelation_age,
               data = training_set)

# predicting thr test results
y_pred = predict(regressor, newdata = test_set)
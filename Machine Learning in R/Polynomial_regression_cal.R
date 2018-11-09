# Polynomial Regression
dataset = read.csv('Test1.csv')

#categorical data
dataset$ids_familyrelation_gender = factor(dataset$ids_familyrelation_gender,
                                           levels = c('Female', 'Male'),
                                           labels = c(0,1))

# Splitting the data set into test set and training set
set.seed(123)
split = sample.split(dataset$calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting the Polynomial Regression to the dataset

dataset$ids_familyrelation_age2 = dataset$ids_familyrelation_age^2
dataset$ids_familyrelation_age3 = dataset$ids_familyrelation_age^3
dataset$ids_familyrelation_age4 = dataset$ids_familyrelation_age^4
poly_reg = lm(formula = dataset$calories ~ dataset$ids_familyrelation_age2 + dataset$ids_familyrelation_age + dataset$ids_familyrelation_age3 + dataset$ids_familyrelation_age4,
              data = training_set)

summary(poly_reg)

#predicting the test results
y_pred = predict(poly_reg, newdata = test_set)


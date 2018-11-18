# Polynomial Regression
dataset = read.csv('compressed_data.csv')
dataset = dataset[7:12]


# Splitting the data set into test set and training set
set.seed(123)
split = sample.split(dataset$Calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting the Polynomial Regression to the dataset

dataset$selection4_familyrelation_age2 = dataset$selection4_familyrelation_age^2
dataset$selection4_familyrelation_age3 = dataset$selection4_familyrelation_age^3
dataset$selection4_familyrelation_age4 = dataset$selection4_familyrelation_age^4

dataset$salary2 = dataset$salary^2
dataset$salary3 = dataset$salary^3
dataset$salary4 = dataset$salary^4

dataset$male2 = dataset$male^2
dataset$male3 = dataset$male^3
dataset$male4 = dataset$male^4

dataset$female2 = dataset$female^2
dataset$female3 = dataset$female^3
dataset$female4 = dataset$female^4

dataset$Count2 = dataset$Count^2
dataset$Count3 = dataset$Count^3
dataset$Count4 = dataset$Count^4

poly_reg = lm(formula = dataset$Calories ~ dataset$selection4_familyrelation_age + dataset$selection4_familyrelation_age2 + dataset$selection4_familyrelation_age3 + dataset$selection4_familyrelation_age4 +
                dataset$salary + dataset$salary2 + dataset$salary3 + dataset$salary4 +
                dataset$male + dataset$male2 + dataset$male3 + dataset$male4 +
                dataset$female + dataset$female2 + dataset$female3 + dataset$female4 +
                dataset$Count + dataset$Count2 + dataset$Count3 +dataset$Count4,
              data = training_set)

summary(poly_reg)

#predicting the test results
pred_PR = predict(poly_reg, newdata = dataset)


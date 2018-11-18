# Multiple Linear regression
 
# Importing the dataset
dataset = read.csv('compressed_data.csv')
dataset = dataset[7:12]


set.seed(123)
library(caTools)

# Splitting the dataset into test set and training set
split = sample.split(dataset$Calories, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting the Multiple Linear Regression model to the training set
regressor = lm(formula = Calories ~ salary + Count + male + female + selection4_familyrelation_age,
               data = training_set)

# predicting thr test results
pred_MR = predict(regressor, newdata = dataset)
#data <- read.csv(file.choose(), header = TRUE)
# data <- cbind(data, pred_MR)
#write.csv(data, "comp.csv")
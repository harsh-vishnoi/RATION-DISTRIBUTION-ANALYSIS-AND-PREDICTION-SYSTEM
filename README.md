# Ration distribution analysis and prediction

A study of how India’s Targeted Public Distribution System (TPDS) allocates food grain, and a model that estimates a household’s calorie need from who lives in the household rather than from an income slab alone.

The National Food Security Act, 2013, uses the TPDS to deliver subsidised grain. Identification of households, leakages, late deliveries, and the same allocation across very different families are the problems this project measured. The proposed RDAP estimate uses gender, age, household size, employment, and income, then clusters households so a fixed amount of grain can be split by need.

The sustainable-development aims called out in the original notes are stronger public institutions, zero hunger, and responsible consumption.

![Public distribution context](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/download.png)

## What is in the repository

| Path | What it is |
| --- | --- |
| `Ration_data/` | CSV stages, from individual records through family totals, regression output, and clusters. `Programs/` has the Python used to compress and update those files |
| `Machine Learning in Python/REGRESSION MAIN/` | Multiple, polynomial, SVR, decision-tree, and random-forest regressions |
| `Machine Learning in Python/REGRESSION VISUALISING/` | The same models on a small test file for plots |
| `Machine Learning in Python/CLUSTERING/` | K-means and the distribution step |
| `Machine Learning in R/` | The same regressions and clustering in R, plus comparison CSVs |
| `Ration/` | React Native 0.56 client (sign-in, profile, activity) with Firebase 4 |
| `Readme/` | Charts linked below |

Poverty headcount used as background (percent):

| Year | Rural | Urban | Total |
| --- | --- | --- | --- |
| 1993–94 | 50.1 | 31.8 | 45.3 |
| 2004–05 | 41.8 | 25.7 | 37.2 |
| 2011–12 | 25.7 | 13.7 | 21.9 |

## Method

1. Assemble household records in `Ration_data/`.
2. Fit regressions for total household calories from age, gender, and the number of people.
3. Compare percentage error across Python and R.
4. Cluster on predicted calories and household income. The elbow plot supported 8 clusters.
5. Divide the ration across those clusters (`CLUSTERING/distribution.py`, `Machine Learning in R/output/`).

The React Native app was the intended place to tie a household to Aadhaar and to record a collection. The screens in `Ration/` are sign-in, sign-up, profile, and activity. They are a 2018 React Native project (`react-native` 0.56, `firebase` 4) and are separate from the notebooks and scripts that produced the error table.

## Error on predicted household calories

Best result in the original run: random forest in Python, 2.31% error.

| Method | Software | Percentage error |
| --- | --- | --- |
| Random forest | Python | 2.31% |
| Random forest | R | 3.85% |
| Polynomial regression | Python | 3.97% |
| Polynomial regression | R | 4.02% |
| SVR | R | 4.59% |
| Multiple regression | Python | 5.64% |
| Multiple regression | R | 5.73% |
| Decision tree | R | 7.02% |
| SVR | Python | 46.57% |

![Elbow method](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/elbow.jpg)

![Regression visualisation](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/Graph1%20for%20visualising%20the%20data.png)

![Second visualisation](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/Graph2%20for%20visualising%20the%20data.png)

Python scripts were run in Spyder. R scripts were run in RStudio. Paths inside the scripts point at the CSV names in the same folder. Run a regression script from its own directory so the relative CSV path resolves.

## References

1. Bhavya Goswami, OneWorld Foundation India. *e-PDS Portal of India: Leveraging technology to provide reliable and timely information on Public Distribution System.*
2. Deepak Ahluwalia. *Public distribution of food in India: Coverage, targeting and leakages.*

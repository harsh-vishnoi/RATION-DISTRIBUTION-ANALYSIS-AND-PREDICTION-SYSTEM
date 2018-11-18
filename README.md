# RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM

## **Overview**

During September 2013, Parliament passed the National Food Security Act (NFSA), 2013. The NFSA seeks to make the right to food a legal entitlement by providing subsidised food grains to nearly two-thirds of the population. The Act relies on the existing Targeted Public Distribution System (TPDS) mechanism to deliver these entitlements. But this method has many loopholes as discussed below. Here in our project we have tried to find those loopholes and propose a better and more accurate method of ration distribution.

## **Sustainable Goals**

   1. Strong institution (Remove corruption)
   2. Zero hunger
   3. Responsible consumption and production

![alt text](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/download.png)


## **Introduction**

   The Public Distribution System (PDS) evolved as a system of management of scarcity and for distribution of food grains at affordable prices. But this system could not achieve its desired objectives because of widespread corruption. So to remove the loopholes of this system, government re-launched the Targeted Public Distribution System (TPDS) in June, 1997 with focus on the poor. Under the TPDS, States were required to formulate and implement foolproof arrangements for the identification of the poor for delivery of food grains. This programme is run by the ministry of consumer affairs, Govt. of India.But TPDS also had same loopholes and problems. TPDS has been criticised on the following grounds:
       
**Operational issues:** (Identification in practice.) The fact of the matter is that the whole process of identification of BPL families in many States has been carried out in a very arbitrary manner. As a result, there have been large errors of misclassification with genuinely deserving households excluded and some affluent households included in the BPL category.

   * Leakages and diversion.
   * Late and irregular arrival of grains in fair price shops.
   * No variation in purchase across expenditure groups.
   * Decline in offtake and the question of viability of fair price shops.
   * TPDS has failed in transferring cereals from surplus to deficit regions.
   * Burden of subsidy has increased.

## **How our method is overcoming the above problems :**

The RDAP (Ration Distribution Analysis and Prediction) system has included many factors, like gender, age, number of people in the family, whether employed or not and hence their salary, and the requirement of calories of an individual according to the standard laws, which has helped us to reach a more accurate prediction of requirements of food.
Many a times the ration provided by Govt. of India is received in very less amount. By this method we are proposing an estimate (but accurate to a great extent) that how much ration is required by people.
Adhaar card of every person in the family is linked with this app which helps in data verification. The entries of people after the ration is bought is stored in the app which would help to remove the corruption.

# METHODOLOGY

   1. DATA SCRAPING
   2. ALGORITHM APPLICATION
   3. TRYING TO VISUALISE THE REGRESSION
   4.	COMPRESSING THE DATA
   5.	APPLYING REGRESSION MODEL
   6. CLUSTERING
   7.	DIVISION OF RATION ACCORDING TO CLUSTERS
   

# CONCLUSION

Concludingly, this project is a new outlook in the field of Ration Distribution to the underprivileged in India. Because, instead of just keeping the Salary Slabs in minds, a incorporates a bigger list of features such as count of people in his family, their genders, total income of a family and their age. This can be a revolutionary approach as having the same amount of Ration to distribute as it was earlier, it is now being distributed more strategically and efficiently. 
This project gave all four of us a great opportunity to look deeper into many Machine Learning algorithms like Multiple, Polynomial, Support Vector, Decision Tree , Random Forest Regression and K- Means Clustering Algorithm.


| Year | Rural | Urban | Total | 
|------|-------|-------|-------|
|1993-94|50.1|31.8|45.3|
|2004-05|41.8|25.7|37.2|
|2011-12|25.7|13.7|21.9|

# RESULTS

The best among these is obtained by Random forest using the python software. This data is the error in total calories of a    family when we have considered the factors : age, gender, number of male and females in a family and total number of people in the family to predict the total requirement of calories of a family.
Next we have made clusters considering two factors which are the total predicted calories from the above step and the total income of all the family members. 
According to this we obtained 8 clusters using the Elbow method.


![alt text](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/elbow.jpg)

 * Hardware / Software requirements

 	1. Python : Spyder
	2. R : R studio
	3. React Native
	4. Firebase
	5. Javascript
  
  * Screenshot Table
  
|Methods / Software| Percentage Error |
|-----|-----|
|Random Forest / py|2.31%|
|Random Forest / R|3.85%|
|Multiple Reg. / py|5.64%|
|Multiple Reg. / R|5.73%|
|SVR / py|46.57%|
|SVR / R|4.59%|
|Decision Tree / R|7.02%|
|Polynomial Reg. / py|3.97%|
|Polynomial Reg. / R|4.02%|

![alt text](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/Graph1%20for%20visualising%20the%20data.png)

![alt text](https://github.com/harsh-vishnoi/RATION-DISTRIBUTION-ANALYSIS-AND-PREDICTION-SYSTEM/blob/master/Readme/Graph2%20for%20visualising%20the%20data.png)


# References
We referred some Research Papers like:

1. e-PDS Portal of India Leveraging technology to provide reliable and timely 
	information on Public Distribution System
   By: Bhavya Goswami, OneWorld Foundation India
2.	Public distribution of food in India: Coverage, targeting and leakages
   By: Deepak Ahluwalia

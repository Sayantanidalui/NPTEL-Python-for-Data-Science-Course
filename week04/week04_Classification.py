# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 18:09:54 2026

@author: User
"""

# CLASSIFYING PERSONAL INCOME 
# =============================================================================
################################# Required packages ############################
# To work with dataframes
import pandas as pd 

# To perform numerical operations
import numpy as np

# To visualize data
import seaborn as sns

#import matplotlib
import matplotlib.pyplot as plt

# To partition the data
from sklearn.model_selection import train_test_split

# importing the library of KNN
from sklearn.neighbors import KNeighborsClassifier  

# Importing performance metrics - accuracy score & confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix


# Importing library for logistic regression
from sklearn.linear_model import LogisticRegression
###############################################################################
# =============================================================================
# Importing data
# =============================================================================
data= pd.read_csv('C:/Users/User/Downloads/income(1).csv',na_values=[" ?"]) 

# =============================================================================
# Data pre-processing
# =============================================================================

data.info()
data.isnull().sum()
data.describe()
data.describe(include='O').T
data['JobType'].value_counts()
data['occupation'].value_counts()



missing = data[data.isnull().any(axis=1)]
print(missing)
# axis=1 => to consider at least one column value is missing in a row

""" Points to note:
1. Missing values in Jobtype    = 1809
2. Missing values in Occupation = 1816 
3. There are 1809 rows where two specific 
   columns i.e. occupation & JobType have missing values
4. (1816-1809) = 7 => You still have occupation unfilled for 
   these 7 rows. Because, jobtype is Never worked
"""

data2 = data.dropna(axis=0)


# =============================================================================
# Cross tables & Data Visualization
# =============================================================================
# Extracting the column names
data2.columns   

# =============================================================================
# Gender proportion table:
# =============================================================================
gender = pd.crosstab(index = data2["gender"], columns  = 'count', normalize = True)
print(gender)
# =============================================================================
#  Gender vs Salary Status:
# =============================================================================
gender_salstat = pd.crosstab(index = data2["gender"],columns = data2['SalStat'], margins = True, normalize =  'index') 
                 # Include row and column totals
print(gender_salstat)

# =============================================================================
# Frequency distribution of 'Salary status' 
# =============================================================================
SalStat = sns.countplot(data2['SalStat'])

"""  75 % of people's salary status is <=50,000 
     & 25% of people's salary status is > 50,000
"""

##############  Histogram of Age  #############################
sns.distplot(data2['age'], bins=10, kde=False)
# People with age 20-45 age are high in frequency

############# Box Plot - Age vs Salary status #################
sns.boxplot('SalStat', 'age', data=data2)
data2.groupby('SalStat')['age'].median()

## people with 35-50 age are more likely to earn > 50000 USD p.a
## people with 25-35 age are more likely to earn <= 50000 USD p.a

#*** Jobtype
JobType     = sns.countplot(y=data2['JobType'],hue = 'SalStat', data=data2)
job_salstat =pd.crosstab(index = data2["JobType"],columns = data2['SalStat'], margins = True, normalize =  'index')  
round(job_salstat*100,1)


#*** Education
Education   = sns.countplot(y=data2['EdType'],hue = 'SalStat', data=data2)
EdType_salstat = pd.crosstab(index = data2["EdType"], columns = data2['SalStat'],margins = True,normalize ='index')  
round(EdType_salstat*100,1)

#*** Occupation
Occupation  = sns.countplot(y=data2['occupation'],hue = 'SalStat', data=data2)
occ_salstat = pd.crosstab(index = data2["occupation"], columns =data2['SalStat'],margins = True,normalize = 'index')  
round(occ_salstat*100,1)

#*** Capital gain
sns.distplot(data2['capitalgain'], bins = 10, kde = False)

sns.distplot(data2['capitalloss'], bins = 10, kde = False)



# LOGISTIC REGRESSION
# =============================================================================

# Reindexing the salary status names to 0,1
data2['SalStat']=data2['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data2['SalStat'])

new_data=pd.get_dummies(data2, drop_first=True)

# Storing the column names 
columns_list=list(new_data.columns)
print(columns_list)

# Separating the input names from data
features=list(set(columns_list)-set(['SalStat']))
print(features)

# Storing the output values in y
y=new_data['SalStat'].values
print(y)

# Storing the values from input features
x = new_data[features].values
print(x)

# Splitting the data into train and test
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3, random_state=0)

# Make an instance of the Model
logistic = LogisticRegression()

# Fitting the values for x and y
logistic.fit(train_x,train_y)

logistic.coef_
logistic.intercept_

# Prediction from test data
prediction = logistic.predict(test_x)
print(prediction)

# Confusion matrix
confusion_matrix = confusion_matrix(test_y, prediction)
print(confusion_matrix)

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)
print(accuracy_score)

# Printing the misclassified values from prediction

print('Misclassified samples: %d' % (test_y != prediction).sum())

#====================================================================================================================

data3=data.copy()
# =============================================================================
# LOGISTIC REGRESSION - REMOVING INSIGNIFICANT VARIABLES
# =============================================================================

# Reindexing the salary status names to 0,1
data3['SalStat']=data3['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data3['SalStat'])

cols = ['gender','nativecountry','race','JobType']
new_data = data3.drop(cols,axis = 1)

new_data=pd.get_dummies(new_data, drop_first=True)

# Storing the column names 
columns_list2=list(new_data.columns)
print(columns_list2)

# Separating the input names from data
features2=list(set(columns_list2)-set(['SalStat']))
print(features2)

# Storing the output values in y
y2=new_data['SalStat'].values
print(y2)

# Storing the values from input features
x2 = new_data[features2].values
print(x2)

# Splitting the data into train and test
train_x2,test_x2,train_y2,test_y2 = train_test_split(x2,y2,test_size=0.3, random_state=0)

# Make an instance of the Model
logistic2 = LogisticRegression()

# Fitting the values for x and y
logistic2.fit(train_x2,train_y2)

# Prediction from test data
prediction2 = logistic2.predict(test_x2)
print(prediction2)


# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction2)
print(accuracy_score)

# Printing the misclassified values from prediction
print('Misclassified samples: %d' % (test_y2 != prediction2).sum())


#====================================================================================================



# =============================================================================
# KNN
# =============================================================================

# Storing the K nearest neighbors classifier
KNN_classifier = KNeighborsClassifier(n_neighbors = 5)  

# Fitting the values for X and Y
KNN_classifier.fit(train_x, train_y) 

# Predicting the test values with model
prediction = KNN_classifier.predict(test_x)

# Performance metric check
confusionMmatrix = confusion_matrix(test_y, prediction)
print(confusionMmatrix)

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)
print(accuracy_score)

print('Misclassified samples: %d' % (test_y != prediction).sum())

"""
Effect of K value on classifier
"""
Misclassified_sample = []
# Calculating error for K values between 1 and 20
for i in range(1, 20):  
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_x, train_y)
    pred_i = knn.predict(test_x)
    Misclassified_sample.append((test_y != pred_i).sum())

print(Misclassified_sample)









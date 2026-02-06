# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 18:51:18 2026

@author: Sayantani
"""

### WEEK ASSIGNMENT ###

#Q1 correct approach to fill missing values in case of categorical variable --- MODE

#Q2 which are used to extract the column 'Type' as a separate dataframe --- df_cars[['Type]] , df_cars.loc[:,['Type]]

#Q3 df_cars.describe() will give description of which column ---- Price(in lakhs)

#Q4 which pandas function is used to stack the dataframe vertically --- pd.concat()

#Q5 which of the following are libraries in python --- All pf the above(Pandas, Matplotlib, Numpy)

#Q6, Q7, Q8, Q9
import pandas as pd
df_cocoa=pd.read_csv('C:/Users/User/Downloads/flavors_of_cocoa (1).csv',index_col=0)
df_cocoa.info() #Review Date has null values
df_cocoa['Company Location'].value_counts() #which location has maximum companies
df_cocoa.info() #Review date requires a data conversion
df_cocoa['Rating'].max() #maximum rating of chocolate

#Q10
import numpy as np
B=[True,2,20.,np.nan,"False"]
[type(i) for i in B]

#Q11 df.info() provide --- Summary of the dataframe, including the number of non-null entries

#Q12
arr=np.array([1,2,3,4,5])
print(arr[::2])


### PRACTICE ASSIGNMENT ###

#Q1 SCATTER PLOT OF MPG AND WT AND THEN ANS
import matplotlib.pyplot as plt
car=pd.read_csv('C:/Users/User/Downloads/mtcars.csv')
plt.scatter(car['mpg'],car['wt'],c='red')

#Q2 BOX PLOT OF PRICE AND CUT THEN FIND WHICH HAVE HIGHEST MEDIAN PRICE
import seaborn as sns
diamond=pd.read_csv('C:/Users/User/Downloads/diamond.csv')
sns.boxplot(x=diamond['price'],y=diamond['cut'])

#Q3 TOTAL NO OF MISSING VALUES OF THE VARIBALE TOTALCHARGES
churn=pd.read_csv('C:/Users/User/Downloads/churn.csv')
churn['TotalCharges'].isnull().sum()

#Q4 WHICH IS USED TO LINE PLOT FROM THE PACKAGE MATPLOTLIB----PLOT()

#Q5 THE PROBABILITY OF TWO DIFFERENT EVENTS OCCURING AT THE SAME TIME IS KNOWN AS ---- JOINT PROBABILITY

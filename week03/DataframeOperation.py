# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 18:18:21 2026

@author: Sayantani
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data=pd.read_csv('C:/Users/User/Downloads/Toyota.csv',index_col=0)
#create copy
cars_data1=cars_data.copy(deep=True)

#attributes
cars_data1.index
cars_data1.columns
cars_data1.size
cars_data1.shape
cars_data1.memory_usage()
cars_data1.ndim
cars_data1.head(6)
cars_data1.tail(5)
cars_data1.at[4,'FuelType']
cars_data1.iat[5,6]
cars_data1.loc[:,'FuelType']
cars_data1.dtypes
cars_data1.dtypes.value_counts()

cars_data1.select_dtypes(exclude=[object])
cars_data1.info()

print(np.unique(cars_data1['KM']))
print(np.unique(cars_data1['HP']))
print(np.unique(cars_data1['MetColor']))
print(np.unique(cars_data1['Automatic']))
print(np.unique(cars_data1['Doors']))

cars_data=pd.read_csv('C:/Users/User/Downloads/Toyota.csv',index_col=0,na_values=["??","????"])
cars_data.info()

cars_data['MetColor']=cars_data['MetColor'].astype('object')
cars_data['Automatic']=cars_data['Automatic'].astype('object')

cars_data['FuelType'].nbytes

cars_data.info()

cars_data['Doors'].replace('three',3,inplace=True)

cars_data['Doors'].replace('four',4,inplace=True)

cars_data['Doors'].replace('five',5,inplace=True)

cars_data['Doors']=cars_data['Doors'].astype('int64')

cars_data.info()

cars_data.isnull().sum()
cars_data1=cars_data.copy(deep=True)

cars_data1.insert(10,"Price_Class","")

for i in range(0,len(cars_data1['Price']),1):
    if(cars_data1['Price'][i]<=8450):
        cars_data1['Price_Class'][i]="Low"
    elif(cars_data1['Price'][i]>11950):
        cars_data1['Price_Class'][i]="High"
    else : cars_data1['Price_Class'][i]="Medium"

cars_data1['Price_Class'].value_counts()


#convert age from months to years

cars_data1.insert(11,"Age_converted",0)

def c_convert(val):
     val_convert=val/12
     return val_convert

cars_data1["Age_converted"]=c_convert(cars_data1['Age'])
cars_data1["Age_converted"]=round(cars_data1["Age_converted"],1)

#km per month
cars_data1.insert(12,"Km_per_month",0)

def c_convert(val1,val2):
    val_convert=val1/12
    ratio=val2/val1
    return [val_convert,ratio]

cars_data1["age_converted"],cars_data1["Km_per_month"]=c_convert(cars_data1['Age'],cars_data1['KM'])

cars_data1.drop('age_converted',axis=1,inplace=True)


cars_data2=cars_data.copy()
cars_data3=cars_data2.copy()


pd.crosstab(index=cars_data2['FuelType'],columns='count',dropna=True)
#most of the cars have petrol as fuel type


pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True)
#only petrol fueltype cars have automatic gearbox

pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize=True,dropna=True)


pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],margins=True,normalize=True,dropna=True)

pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],margins=True,normalize='index',dropna=True)

pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],margins=True,normalize='columns',dropna=True)

numerical=cars_data2.select_dtypes(exclude=[object])
print(numerical.shape)

corr=numerical.corr()


#visualize

cars_data.dropna(axis=0, inplace=True)
#Scatter plot
plt.scatter(cars_data['Age'],cars_data['Price'],c='red')
plt.title('Scatter plot of price vs Age of the cars')
plt.xlabel('Age(months)')
plt.ylabel('Price(Euros)')
plt.show()

#histrogram
plt.hist(cars_data['KM'], color='green', edgecolor='white', bins=5)
plt.title('Histrogram of kilometer')
plt.xlabel('kilometer')
plt.ylabel('Frequency')
plt.show()

#barplot
index=['petrol','diesel','cng']
col=[922,450,220]
plt.bar(index,col,color=['red','blue','cyan'])
plt.title('Bar plot of Fuel Type')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.show()

#scatter plot of seaborn
sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age'],y=cars_data['Price'],fit_reg=False,marker="*")

sns.lmplot(x='Age', y='Price', data=cars_data,fit_reg=False,hue='FuelType',legend=True,palette="Set1")

#histrogram of seaborn
sns.distplot(cars_data['Age'],kde=False,bins=5)
cars_data['FuelType'].value_counts()
cars_data['FuelType'].value_counts().plot(kind='bar')

#barplot of seaborn
sns.countplot(x="FuelType",data=cars_data,hue="Automatic")

#boxplot of seaborn
sns.boxplot(y=cars_data['Price'])

sns.boxplot(x=cars_data['FuelType'],y=cars_data['Price'])

sns.boxplot(x=cars_data['FuelType'],y=cars_data['Price'],hue=cars_data['Automatic'])

#split the window
f,(ax_box, ax_hist)=plt.subplots(2, gridspec_kw={"height_ratios":(.35,.85)})
sns.boxplot(cars_data["Price"], ax=ax_box)
sns.distplot(cars_data["Price"], ax=ax_hist, kde=False)

#pairwise plot
sns.pairplot(cars_data, kind="scatter",hue="FuelType")
plt.show()


#dealing with missing values
 
cars_data2.isnull().sum()

missing=cars_data2[cars_data2.isnull().any(axis=1)]

#numeric data
cars_data2.describe()
cars_data2['Age'].fillna(cars_data2['Age'].mean(),inplace=True)
cars_data2['KM'].fillna(cars_data2['KM'].median(),inplace=True)
cars_data2['HP'].fillna(cars_data2['HP'].mean(),inplace=True)

#categorical data

cars_data2['FuelType'].value_counts().index[0]
cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0],inplace=True)

cars_data2['MetColor'].mode()

cars_data2['MetColor'].fillna(cars_data2['MetColor'].mode()[0],inplace=True)

cars_data2.isnull().sum()


#fill in one shot

cars_data3=cars_data3.apply(lambda x:x.fillna(x.mean())if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
cars_data3.isnull().sum()













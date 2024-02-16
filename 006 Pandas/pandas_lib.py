# Pandas library used for data processing

#pandas dataframe is a 2D tabular data structure with labeled axes
import pandas as pd

#creating a pandas dataframe

#importing boston house price data
from sklearn.datasets import load_boston
boston_dataset=load_boston()
print(boston_dataset)

print("now dataframe will represent this randomly written dataset in a proper tabular shape")
 #pandas dataframe
boston_df=pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)

print(boston_df.head()) #head will print 1st 5 data
print(boston_df.shape)


#inspecting a dataframe

#shape of df

print(boston_df.shape)

#first 5 rows of df

print(boston_df.head())

# Last 5 rows of df

print(boston_df.tail())

#information about df
print(boston_df.info())

#finding no of missing values to boston df
print(boston_df.isnull().sum())

#Statistical measures

#count no of values
print(boston_df.count())

#coloumwise mean

print(boston_df.mean())

#coloumn wise standard deviation

print(boston_df.std())

# min value at each coloumn

print(boston_df.min())

# Max value at each coloumn

print(boston_df.max())

#all the statistical measure about dataframe
print(boston_df.describe())


#adding a coloumn to a dataframe
boston_df['Price']=boston_dataset.target
print(boston_df.head())

#removing a row
print(boston_df.drop(index=0,axis=0))
#removing a coloumn
print(boston_df.drop(columns='CRIM',axis=1))

#Loacting a row using index value
print(boston_df.iloc[2])

# Locating a particular coloumn

print(boston_df.iloc[:,0]) #first cloumn
print(boston_df.iloc[:,1]) #second_coloumn
print(boston_df.iloc[:,2]) #third coloumn
print(boston_df.iloc[:,-1]) #Last coloumn


#Co-relation:-relationship b/w two coloumns of table
#two types:-1>positive corelaton 2>negative coprelation
print(boston_df.corr())
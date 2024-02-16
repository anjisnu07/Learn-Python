# The process of standardizing the data to a common format and a common range
import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# loading the dataset

dataset=sklearn.datasets.load_breast_cancer()
print(dataset)

df=pd.DataFrame(dataset.data,columns=dataset.feature_names)
print(df.head())

print(df.shape)

x=df
y=dataset.target

print(x)
print(y)

# Spliting into train data and test data

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=3) #0.2 means 20 percent

print(x.shape,x_train.shape,x_test.shape)

# Standardizing the data

# Finding standard deviation..if the range of data is within same range std deviation will be nearly 1
print(dataset.data.std())

scalar=StandardScaler()
scalar.fit(x_train)
x_train_standardized=scalar.transform(x_train)
print(x_train_standardized)

x_test_standardized=scalar.transform(x_test)

print(x_train_standardized.std()) # Standard deviation is 1
print(x_test_standardized.std())
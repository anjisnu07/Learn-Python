# Training data usedfor training purpose where as testing data for test 
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
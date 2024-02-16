import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df=pd.read_csv('015 Numerical Dataset preprocessing\diabetes.csv')
print(df.head())
print(df.shape)
print(df.describe)

# Separating features and target

x=df.drop(columns=['Outcome'],axis=1)
y=df['Outcome']
print(x)
print(y)

# Standardizing data

scalar=StandardScaler()
scalar.fit(x)
x_standardize=scalar.transform(x)
print(x_standardize)
x=x_standardize

# Splitting into training and testing data

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)
print(x.shape,x_train.shape,x_test.shape)
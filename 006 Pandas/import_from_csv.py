#csv file to padnas df
import pandas as pd
from sklearn.datasets import load_boston

# Provide the full path to the diabetes.csv file
diabetes_df = pd.read_csv('C:/Users/royan/Desktop/Complete ML from scratch/006 Pandas/diabetes.csv') #reading a csv file

print(type(diabetes_df))
print(diabetes_df.head())
print(diabetes_df.shape)


boston_dataset=load_boston()
boston_df=pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
print(boston_df)
#export dataframe to a csv file
boston_df.to_csv('boston.csv')

#count the values based on label

print(diabetes_df.value_counts('Outcome'))

#group the values based on label/mean

print(diabetes_df.groupby('Outcome').mean())
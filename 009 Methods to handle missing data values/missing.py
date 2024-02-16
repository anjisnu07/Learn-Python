# Two methods to do that--1>imputation:->fill with statestical data 2> dropping,drop those coloumn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading dataset to pandas dataframe
df = pd.read_csv('C:\\Users\\royan\\Desktop\\Complete ML from scratch\\009 Methods to handle missing data values\\Placement_Dataset.csv')

print(df.head())
print(df.shape)
print(df.isnull().sum())

# As total 215 data is there so we dont drop it,we wil use imputation method
#Central tendencies:-mean,median,mode

# Analysing data using plot

ax,figure=plt.subplots(figsize=(8,8))
sns.displot(df.salary)
plt.show() 
# the output is a skew format,means its not distributed.so we cant apply mean,we will apply median or mode

# Replacing using median value
df['salary'].fillna(df['salary'].median(),inplace=True)

print(df.isnull().sum()) #This show no missing value is there




# Dropping method-it's not reccomended for small dataset
salary= pd.read_csv('C:\\Users\\royan\\Desktop\\Complete ML from scratch\\009 Methods to handle missing data values\\Placement_Dataset.csv')
print(salary.isnull().sum())
salary=salary.dropna(how='any')
print(salary.isnull().sum())
print(salary.shape)
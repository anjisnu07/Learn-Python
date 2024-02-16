# Seaborn :- Data visualisation library

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Loading a inbuilt dataset
tips=sns.load_dataset('tips')
print(tips.head())
# This will plot the graph.x=xaxis val,y=yaxis val,col= it will separate in different coloumns wrt to diff time,hue
#means it will be diffirentiate wrt to smoker,i.e if smoker true then another color if false the another

sns.relplot(data=tips, x='total_bill', y='tip', col='time', hue='smoker', style='smoker', size='size')
plt.show()

# Loading iris dataset
iris=sns.load_dataset('iris')
print(iris.head())
# scatter plt:->Cluster same type of data
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)
plt.show()

# Loading titanic dataset
titaic=sns.load_dataset('titanic')
print(titaic.head())

# Count plot:->plots count only
sns.countplot(x='class',data=titaic)
plt.show()
sns.countplot(x='survived',data=titaic)
plt.show()

# Bar plot
sns.barplot(x='sex',y='survived',hue='class',data=titaic)
plt.show()

# House proce dataset
from sklearn.datasets import load_boston
house_dataset=load_boston()
house=pd.DataFrame(house_dataset.data,columns=house_dataset.feature_names)
house['PRICE']=house_dataset.target

print(house.head())
# Distribution plot
sns.displot(house['PRICE'])
plt.show()
# distribution plot with probablity curve
sns.distplot(house['PRICE'])
plt.show()

# Corelation
corelation=house.corr()
# Construction a heatmape to show corelation
plt.figure(figsize=(10,10))
# corelation is for corelation var,cbar is colour bar,fmt '.1f' means 1 floating point after decimal,i.e 8.1
# annot means annotation in side like CRIM ZN etc and annot_kws is anotation size,cmap is colour blue

sns.heatmap(corelation,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')
plt.show()


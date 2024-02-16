import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Label encoding for breast cancer

cancer_data = pd.read_csv('C:\\Users\\royan\\Desktop\\Complete ML from scratch\\011 Label Encoding\\breast_cancer_data.csv')


print(cancer_data.head())

#Finding count of diff labels
cancer_data['diagnosis'].value_counts()

# Load label encoder function
Label_encode = LabelEncoder()
labels=Label_encode.fit_transform(cancer_data.diagnosis)
cancer_data['target']=labels

print(cancer_data.head()) #Labels will be given in alphabatical order.As B comes before M so b will be labeled by 0 and M will be by 1



# Label encoding for iris dataset

df=pd.read_csv('011 Label Encoding\iris_data.csv')
print(df.head())

print(df['Species'].value_counts())
# Label encoding

label_encode2=LabelEncoder()
labels2=label_encode2.fit_transform(df.Species)
df['target']=labels2
print(df.head())
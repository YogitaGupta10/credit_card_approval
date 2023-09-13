# -*- coding: utf-8 -*-
"""Credit Card approval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/139mo-sEXwhc1qsQLrFoFnXex9R31DNUa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/content/cc_approvals.data',header=None)

df.head()

df.info()

df.describe()

df.isnull().sum()

df.columns

df.eq(0).sum()

df.duplicated().sum()

df= df.replace('?',np.NaN)

df.isnull().sum()

for col in df.columns:
  if df[col].dtypes == 'object':
        df = df.fillna(df[col].value_counts().index[0])

df.isnull().sum()

df.nunique()

df = df.drop([11, 13], axis=1)

df = pd.get_dummies(df)

df.head()

df.shape

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler

df_X_train, df_X_test = train_test_split(df, test_size=0.33, random_state=42)

X_train, y_train = df_X_train.iloc[:, :-1].values, df_X_train.iloc[:, [-1]].values
X_test, y_test = df_X_test.iloc[:, :-1].values, df_X_test.iloc[:, [-1]].values

scaler = MinMaxScaler(feature_range=(0,1))
rescaledX_train = scaler.fit_transform(X_train)
rescaledX_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression

lr= LogisticRegression()
lr.fit(rescaledX_train, y_train)

y_pred= lr.predict(rescaledX_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)

print(confusion_matrix(y_test,y_pred))

from sklearn.ensemble import RandomForestClassifier

rf= RandomForestClassifier()
rf.fit(rescaledX_train, y_train)

y_pred2= rf.predict(rescaledX_test)

accuracy_score(y_test, y_pred2)

print(confusion_matrix(y_test,y_pred2))

